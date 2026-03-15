from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Tuple

@dataclass
class TwoBodyThermalSystem:
    m1: float
    c1: float
    m2: float
    c2: float
    K: float
    T1_initial: float
    T2_initial: float

    @property
    def C1(self) -> float:
        return self.m1 * self.c1

    @property
    def C2(self) -> float:
        return self.m2 * self.c2

    def derivatives(self, T1: float, T2: float) -> Tuple[float, float]:
        dT1_dt = -(self.K / self.C1) * (T1 - T2)
        dT2_dt = +(self.K / self.C2) * (T1 - T2)
        return dT1_dt, dT2_dt

    def equilibrium_temperature(self) -> float:
        return (self.C1 * self.T1_initial + self.C2 * self.T2_initial) / (self.C1 + self.C2)

    def rate_constant(self) -> float:
        return self.K * (1.0 / self.C1 + 1.0 / self.C2)

    def analytic_solution(self, t: float) -> Tuple[float, float]:
        Teq = self.equilibrium_temperature()
        lam = self.rate_constant()
        T1 = Teq + (self.T1_initial - Teq) * math.exp(-lam * t)
        T2 = Teq + (self.T2_initial - Teq) * math.exp(-lam * t)
        return T1, T2
