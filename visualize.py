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
    # Convert Qobj → numeric array
    mat = rho.full()  # or np.array(rho.full())

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Real part
    im0 = axes[0].imshow(np.real(mat), cmap='viridis')
    axes[0].set_title("Real part")
    axes[0].set_xlabel("Column")
    axes[0].set_ylabel("Row")
    fig.colorbar(im0, ax=axes[0])

    # Imaginary part
    im1 = axes[1].imshow(np.imag(mat), cmap='viridis')
    axes[1].set_title("Imaginary part")
    axes[1].set_xlabel("Column")
    axes[1].set_ylabel("Row")
    fig.colorbar(im1, ax=axes[1])

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
