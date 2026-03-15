from __future__ import annotations
import matplotlib.pyplot as plt

def plot_temperatures(times, T1, T2, title, method="euler", save_path=None):
    # Boje po metodi
    color_map = {
        "euler": ("tab:blue", "tab:orange"),
        "heun": ("tab:purple", "tab:brown"),
        "rk4": ("tab:green", "tab:red"),
    }

    c1, c2 = color_map.get(method.lower(), ("black", "gray"))

    plt.figure()
    plt.plot(times, T1, color=c1, linestyle="-", label="T1(t)")
    plt.plot(times, T2, color=c2, linestyle="--", label="T2(t)")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Temperatura [°C]")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=200)
    plt.show()


def plot_deltaT(times, T1, T2, title, method="euler", save_path=None):
    color_map = {
        "euler": "tab:blue",
        "heun": "tab:purple",
        "rk4": "tab:green",
    }

    c = color_map.get(method.lower(), "black")
    delta = [a - b for a, b in zip(T1, T2)]

    plt.figure()
    plt.plot(times, delta, color=c, label="DeltaT(t)")
    plt.axhline(0.0, linestyle="--", color="black")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Delta T [°C]")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=200)
    plt.show()


def plot_time_to_equilibrium(labels, times_to_eq, threshold, title, save_path=None):

    plt.figure()
    plt.bar(labels, times_to_eq)
    plt.ylabel(f"Vrijeme do ravnoteže [s] (|ΔT| < {threshold}°C)")
    plt.title(title)
    plt.xticks(rotation=15, ha="right")
    plt.grid(True, axis="y")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=200)
    plt.show()




