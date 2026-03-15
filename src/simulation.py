from __future__ import annotations
from typing import Callable, Dict, List, Tuple
import time

from model import TwoBodyThermalSystem
from numerical_methods import euler_step, heun_step, rk4_step, State

StepFunc = Callable[[TwoBodyThermalSystem, State, float], State]

METHODS: Dict[str, StepFunc] = {
    "euler": euler_step,
    "heun": heun_step,
    "rk4": rk4_step,
}

def run_simulation(system: TwoBodyThermalSystem, method: str, t_end: float, dt: float) -> Tuple[List[float], List[float], List[float]]:
    method_key = method.lower().strip()
    if method_key not in METHODS:
        raise ValueError(f"Nepoznata metoda: {method}. Podrzane: {list(METHODS.keys())}")

    step: StepFunc = METHODS[method_key]

    times: List[float] = [0.0]
    T1_list: List[float] = [system.T1_initial]
    T2_list: List[float] = [system.T2_initial]

    t = 0.0
    state: State = (system.T1_initial, system.T2_initial)

    n_steps = int(round(t_end / dt))
    for _ in range(n_steps):
        state = step(system, state, dt)
        t += dt
        times.append(t)
        T1_list.append(state[0])
        T2_list.append(state[1])

    return times, T1_list, T2_list

def final_error_against_analytic(system: TwoBodyThermalSystem, method: str, t_end: float, dt: float) -> Tuple[float, float]:
    _, T1, T2 = run_simulation(system, method, t_end, dt)
    T1_exact, T2_exact = system.analytic_solution(t_end)
    return abs(T1[-1] - T1_exact), abs(T2[-1] - T2_exact)

def measure_runtime(system: TwoBodyThermalSystem, method: str, t_end: float, dt: float, repeats: int = 10) -> float:
    start = time.perf_counter()
    for _ in range(repeats):
        run_simulation(system, method, t_end, dt)
    end = time.perf_counter()
    return (end - start) / repeats
