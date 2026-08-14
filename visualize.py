import matplotlib.pyplot as plt
import numpy as np
import qutip as qt

def bloch_vector_from_density(rho):
    sx = qt.sigmax()
    sy = qt.sigmay()
    sz = qt.sigmaz()

    x = (rho * sx).tr().real
    y = (rho * sy).tr().real
    z = (rho * sz).tr().real

    return np.array([x, y, z])


def bloch_trajectory(states):
    """
    Plot the trajectory of a sequence of single-qubit states on the Bloch sphere.
    states: list of density matrices
    """
    b = qt.Bloch()
    points = []

    for rho in states:
        bloch_vec = bloch_vector_from_density(rho)

        points.append(bloch_vec)

    points = np.array(points).T   # convert list of vectors into 3×N matrix
    b.add_points(points)

    b.make_sphere()
    b.show()

def density_matrix_plot(rho):
    """
    Plot the real and imaginary parts of a density matrix.
    """
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    real = np.real(rho.full())
    imag = np.imag(rho.full())

    axes[0].imshow(real, cmap='viridis')
    axes[0].set_title("Real part")

    axes[1].imshow(imag, cmap='magma')
    axes[1].set_title("Imaginary part")

    plt.tight_layout()
    plt.show()

def fidelity_plot(fidelities):
    """
    Plot fidelity over time.
    fidelities: list of floats
    """
    plt.figure(figsize=(6,4))
    plt.plot(fidelities, marker='o')
    plt.xlabel("Step")
    plt.ylabel("Fidelity")
    plt.title("Fidelity decay under noise")
    plt.grid(True)
    plt.show()
