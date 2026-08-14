import numpy as np
import qutip as qt

# ---------------------------------------------------------
# Helper: apply Kraus operators
# ---------------------------------------------------------
def apply_kraus(rho, kraus_ops):
    out = qt.Qobj(np.zeros((2,2), dtype=complex))
    for K in kraus_ops:
        out += K * rho * K.dag()
    return out


# ---------------------------------------------------------
# Depolarizing channel
# E(ρ) = (1 - p) ρ + p I/2
# ---------------------------------------------------------
def depolarizing(p):
    I = qt.qeye(2)
    def channel(rho):
        return (1 - p) * rho + p * (I / 2)
    return channel


# ---------------------------------------------------------
# Bit-flip channel
# Kraus: sqrt(1-p) I, sqrt(p) X
# ---------------------------------------------------------
def bit_flip(p):
    I = qt.qeye(2)
    X = qt.sigmax()
    K0 = np.sqrt(1 - p) * I
    K1 = np.sqrt(p) * X
    def channel(rho):
        return apply_kraus(rho, [K0, K1])
    return channel


# ---------------------------------------------------------
# Phase-flip channel
# Kraus: sqrt(1-p) I, sqrt(p) Z
# ---------------------------------------------------------
def phase_flip(p):
    I = qt.qeye(2)
    Z = qt.sigmaz()
    K0 = np.sqrt(1 - p) * I
    K1 = np.sqrt(p) * Z
    def channel(rho):
        return apply_kraus(rho, [K0, K1])
    return channel


# ---------------------------------------------------------
# Amplitude damping channel
# Kraus operators:
# K0 = [[1, 0], [0, sqrt(1-gamma)]]
# K1 = [[0, sqrt(gamma)], [0, 0]]
# ---------------------------------------------------------
def amplitude_damping(gamma):
    K0 = qt.Qobj([[1, 0],
                  [0, np.sqrt(1 - gamma)]])
    K1 = qt.Qobj([[0, np.sqrt(gamma)],
                  [0, 0]])
    def channel(rho):
        return apply_kraus(rho, [K0, K1])
    return channel


# ---------------------------------------------------------
# Phase damping (pure dephasing)
# Kraus:
# K0 = sqrt(1-p) I
# K1 = sqrt(p) |0><0|
# K2 = sqrt(p) |1><1|
# ---------------------------------------------------------
def phase_damping(p):
    I = qt.qeye(2)
    P0 = qt.basis(2,0) * qt.basis(2,0).dag()
    P1 = qt.basis(2,1) * qt.basis(2,1).dag()
    K0 = np.sqrt(1 - p) * I
    K1 = np.sqrt(p) * P0
    K2 = np.sqrt(p) * P1
    def channel(rho):
        return apply_kraus(rho, [K0, K1, K2])
    return channel
