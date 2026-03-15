from __future__ import annotations
from typing import Dict, List, Tuple
from model import TwoBodyThermalSystem
from simulation import final_error_against_analytic, measure_runtime

def error_sweep(system: TwoBodyThermalSystem, t_end: float, dts: List[float], methods: List[str]) -> Dict[str, List[Tuple[float, float, float]]]:
    out: Dict[str, List[Tuple[float, float, float]]] = {}
    for m in methods:
        rows = []
        for dt in dts:
            e1, e2 = final_error_against_analytic(system, m, t_end, dt)
            rows.append((dt, e1, e2))
        out[m] = rows
    return out

def runtime_sweep(system: TwoBodyThermalSystem, t_end: float, dt: float, methods: List[str], repeats: int = 10) -> Dict[str, float]:
    return {m: measure_runtime(system, m, t_end, dt, repeats=repeats) for m in methods}
