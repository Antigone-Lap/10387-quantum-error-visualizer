

import numpy as np
import qutip as qt

def bloch_state(theta, phi):
    """
    Create a single-qubit pure state from Bloch sphere angles.
    |ψ> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>
    """
    alpha = np.cos(theta/2)
    beta = np.exp(1j * phi) * np.sin(theta/2)
    return qt.Qobj([[alpha], [beta]])


def zero_state():
    return qt.basis(2, 0)

def one_state():
    return qt.basis(2, 1)

def plus_state():
    return (qt.basis(2,0) + qt.basis(2,1)).unit()

def minus_state():
    return (qt.basis(2,0) - qt.basis(2,1)).unit()

def density_matrix(state):
    """
    Convert a state vector |psi> into a density matrix rho = |psi><psi|.
    If state is already a density matrix, return it unchanged.
    """
    if state.isket:
        return state * state.dag()
    return state

def cat_state(phase=0):
    """
    Create a simple qubit 'cat' state:
    |cat> = (|0> + e^{i phase} |1>) / sqrt(2)
    """
    return (qt.basis(2,0) + np.exp(1j * phase) * qt.basis(2,1)).unit()

