from channels import apply_kraus
from states import density_matrix
from tqdm import tqdm

def trajectory(rho0, channel, steps):
    """
    Generate a sequence of states by repeatedly applying a noise channel.
    rho0: initial state (ket or density matrix)
    channel: a noise channel function
    steps: number of iterations
    """
    rho = density_matrix(rho0)
    states = [rho]

    for _ in tqdm(range(steps)):
        rho = channel(rho)

        states.append(rho)

    return states

def trajectory_no_tqdm(rho0, channel, steps):
    """
    Same as trajectory(), but without a progress bar.
    """
    rho = density_matrix(rho0)
    states = [rho]

    for _ in range(steps):
        rho = channel(rho)

        states.append(rho)

    return states