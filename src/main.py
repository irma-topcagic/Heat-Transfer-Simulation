from __future__ import annotations

from model import TwoBodyThermalSystem
from simulation import run_simulation, final_error_against_analytic
from visualization import (
    plot_temperatures,
    plot_deltaT,
    plot_time_to_equilibrium,
)
from scenarios import get_scenarios
from analysis import error_sweep, runtime_sweep


def build_system(scen: dict) -> TwoBodyThermalSystem:
    """Kreira fizicki sistem na osnovu parametara scenarija."""
    return TwoBodyThermalSystem(
        m1=scen["m1"], c1=scen["c1"],
        m2=scen["m2"], c2=scen["c2"],
        K=scen["K"],
        T1_initial=scen["T1"], T2_initial=scen["T2"]
    )


def make_safe_name(name: str) -> str:
    bad_chars = [" ", ":", "(", ")", ",", ">", "<", "=", "/", "+"]
    safe = name
    for ch in bad_chars:
        safe = safe.replace(ch, "_")
    return safe


def main():
    # Numericke metode koje se porede
    methods = ["euler", "heun", "rk4"]

    # Ucitavanje scenarija
    scenarios = get_scenarios()

    # Podaci za grafik vremena do ravnoteze
    labels = []
    times_to_eq = []

    # Prag za definiciju termicke ravnoteze
    THRESHOLD = 1.0  

    for scen in scenarios:
        system = build_system(scen)
        safe_name = make_safe_name(scen["name"])

        print("\n" + "=" * 70)
        print(scen["name"])
        print("=" * 70)
        print(f"Ravnotezna temperatura Teq = {system.equilibrium_temperature():.4f} °C")
        print(f"Lambda (stopa) = {system.rate_constant():.6f} 1/s")
        print(f"Simulacija: t_end={scen['t_end']} s, dt={scen['dt']} s")

        # 1) Simulacija i graficki prikaz (po metodi)
        for m in methods:
            times, T1, T2 = run_simulation(system, m, scen["t_end"], scen["dt"])
            e1, e2 = final_error_against_analytic(system, m, scen["t_end"], scen["dt"])

            print(f"[{m.upper()}] T1_end={T1[-1]:.4f}, T2_end={T2[-1]:.4f}, "
                  f"err=({e1:.6f}, {e2:.6f})")

            plot_temperatures(
                times, T1, T2,
                title=f"{scen['name']} - {m.upper()}",
                method=m,
                save_path=f"plot_{safe_name}_{m}_T.png"
            )

            plot_deltaT(
                times, T1, T2,
                title=f"{scen['name']} - {m.upper()} (DeltaT)",
                method=m,
                save_path=f"plot_{safe_name}_{m}_dT.png"
            )

        # 2) Poredjenje greske za razlicite dt
        dts = [5.0, 2.0, 1.0, 0.5, 0.2]
        errors = error_sweep(system, scen["t_end"], dts, methods)

        print("\nGreska u odnosu na analiticko rjesenje (finalno vrijeme)")
        for m in methods:
            print(f"Metoda {m.upper()}:")
            for dt, e1, e2 in errors[m]:
                print(f"   dt={dt:>4}  errT1={e1:.6f}  errT2={e2:.6f}")

        # 3) Performanse (vrijeme izvrsavanja)
        runtimes = runtime_sweep(system, scen["t_end"], scen["dt"], methods, repeats=10)

        print("\nProsjecno vrijeme izvrsavanja (sekunde)")
        for m in methods:
            print(f"   {m.upper()}: {runtimes[m]:.6e} s")

        # 4) Vrijeme do termicke ravnoteze (koristi se RK4)
        times_rk, T1_rk, T2_rk = run_simulation(system, "rk4", scen["t_end"], scen["dt"])

        teq = None
        for t_i, a, b in zip(times_rk, T1_rk, T2_rk):
            if abs(a - b) < THRESHOLD:
                teq = t_i
                break
        if teq is None:
            teq = times_rk[-1]

        labels.append(scen["name"])
        times_to_eq.append(teq)

    # Grafik vremena do ravnoteze
    plot_time_to_equilibrium(
        labels,
        times_to_eq,
        threshold=THRESHOLD,
        title="Vrijeme do termičke ravnoteže po scenarijima (RK4)",
        save_path="time_to_equilibrium.png"
    )


if __name__ == "__main__":
    main()
