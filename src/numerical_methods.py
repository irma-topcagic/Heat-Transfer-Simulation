from __future__ import annotations
from typing import Tuple
from model import TwoBodyThermalSystem

State = Tuple[float, float]  # (T1, T2)

def euler_step(system: TwoBodyThermalSystem, state: State, dt: float) -> State:
    T1, T2 = state
    dT1, dT2 = system.derivatives(T1, T2)
    return (T1 + dt * dT1, T2 + dt * dT2)

def heun_step(system: TwoBodyThermalSystem, state: State, dt: float) -> State:
    T1, T2 = state
    dT1_a, dT2_a = system.derivatives(T1, T2)
    T1_pred = T1 + dt * dT1_a
    T2_pred = T2 + dt * dT2_a
    dT1_b, dT2_b = system.derivatives(T1_pred, T2_pred)
    T1_next = T1 + (dt / 2.0) * (dT1_a + dT1_b)
    T2_next = T2 + (dt / 2.0) * (dT2_a + dT2_b)
    return (T1_next, T2_next)

def rk4_step(system: TwoBodyThermalSystem, state: State, dt: float) -> State:
    T1, T2 = state

    k1_T1, k1_T2 = system.derivatives(T1, T2)

    T1_2 = T1 + 0.5 * dt * k1_T1
    T2_2 = T2 + 0.5 * dt * k1_T2
    k2_T1, k2_T2 = system.derivatives(T1_2, T2_2)

    T1_3 = T1 + 0.5 * dt * k2_T1
    T2_3 = T2 + 0.5 * dt * k2_T2
    k3_T1, k3_T2 = system.derivatives(T1_3, T2_3)

    T1_4 = T1 + dt * k3_T1
    T2_4 = T2 + dt * k3_T2
    k4_T1, k4_T2 = system.derivatives(T1_4, T2_4)

    T1_next = T1 + (dt / 6.0) * (k1_T1 + 2*k2_T1 + 2*k3_T1 + k4_T1)
    T2_next = T2 + (dt / 6.0) * (k1_T2 + 2*k2_T2 + 2*k3_T2 + k4_T2)
    return (T1_next, T2_next)
