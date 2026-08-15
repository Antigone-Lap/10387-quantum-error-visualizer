import matplotlib.pyplot as plt
import numpy as np
import qutip as qt
from matplotlib.animation import FuncAnimation, PillowWriter

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



def bloch_rotating_animation(states):
    """
    Rotating Bloch sphere with moving arrow + trajectory.
    Exportable as GIF using PillowWriter.
    """

    # Convert states → Bloch vectors
    vecs = np.array([
        [
            (rho * qt.sigmax()).tr().real,
            (rho * qt.sigmay()).tr().real,
            (rho * qt.sigmaz()).tr().real
        ]
        for rho in states
    ])

    # Sphere coordinates
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones_like(u), np.cos(v))

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

    def update(i):
        ax.clear()

        # Draw sphere
        ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.2, linewidth=0)

        # Draw trajectory
        ax.plot(vecs[:i+1,0], vecs[:i+1,1], vecs[:i+1,2], color='blue')

        # Draw arrow
        ax.quiver(0,0,0, vecs[i,0], vecs[i,1], vecs[i,2], color='red', linewidth=2)

        # Rotate camera
        ax.view_init(elev=30, azim=i*4)

        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        ax.set_zlim([-1,1])
        ax.set_box_aspect([1,1,1])

    ani = FuncAnimation(fig, update, frames=len(vecs), interval=100)
    plt.close(fig)
    return ani

