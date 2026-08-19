# Quantum Error Visualizer

A Python toolkit for simulating and visualizing how quantum noise channels degrade single-qubit states.

## Overview

Quantum computers are inherently noisy. Qubits interact with their environment, causing decoherence — the gradual loss of quantum information. This project provides a modular framework to simulate five fundamental noise channels and visualize their effects on the Bloch sphere, through fidelity decay, and via density matrix evolution.

## Modules

### `states.py` — Quantum State Creation

Defines single-qubit quantum states using QuTiP:

- `bloch_state(theta, phi)` — create a state from Bloch sphere angles
- `zero_state()`, `one_state()`, `plus_state()`, `minus_state()` — standard computational and superposition basis states
- `cat_state(phase)` — parameterized superposition state
- `density_matrix(state)` — convert a ket to a density matrix

### `channels.py` — Noise Channel Simulation

Implements quantum noise channels using the **Kraus operator formalism**:

```
E(rho) = sum_k  K_k * rho * K_k^dagger
```

| Channel | Parameter | Physical Process |
|---------|-----------|-----------------|
| `depolarizing(p)` | p | Uniform random errors |
| `bit_flip(p)` | p | Classical bit flips (X errors) |
| `phase_flip(p)` | p | Dephasing (Z errors) |
| `amplitude_damping(gamma)` | gamma | Energy decay (T1 relaxation) |
| `phase_damping(p)` | p | Pure dephasing (T2 decay) |

### `simulate.py` — Trajectory Generation

Applies a noise channel repeatedly to generate a sequence of states:

```python
states = trajectory(rho0, channel, steps=30)
# Returns: [rho0, E(rho0), E^2(rho0), ..., E^30(rho0)]
```

### `metrics.py` — Quality Metrics

- `fidelity_curve(rho0, states)` — compute fidelity at each step
- `purity(rho)` — compute purity
- `purity_curve(states)` — purity over time

### `visualize.py` — Plotting and Animation

- `bloch_trajectory(states)` — plot state evolution on the Bloch sphere
- `fidelity_plot(fidelities)` — plot fidelity decay over time
- `density_matrix_plot(rho)` — visualize real and imaginary parts of rho
- `bloch_rotating_animation(states)` — animated Bloch sphere with rotating camera (saves as GIF)

## Project Structure

```
quantum-error-visualizer/
├── states.py          # Quantum state creation
├── channels.py        # Noise channel implementations (Kraus operators)
├── simulate.py        # Trajectory generation
├── metrics.py         # Fidelity and purity metrics
├── visualize.py       # Bloch sphere, fidelity, and density matrix plots
├── QuantumErrorVisualizer-demo.ipynb  # Interactive demo notebook
├── pyproject.toml     # Project configuration and dependencies
└── README.md
```

## Installation

Requires Python 3.11+ and the following dependencies:

```
numpy
qutip
matplotlib
tqdm
```


## Usage

### Quick Start

```python
from states import bloch_state
from channels import depolarizing
from simulate import trajectory
from metrics import fidelity_curve
from visualize import bloch_trajectory, fidelity_plot

# Create an initial state
rho0 = bloch_state(theta=3.14/3, phi=3.14/4)

# Choose a noise channel
channel = depolarizing(p=0.1)

# Simulate
states = trajectory(rho0, channel, steps=30)

# Analyze
fidelities = fidelity_curve(rho0, states)

# Visualize
bloch_trajectory(states)
fidelity_plot(fidelities)
```

### Jupyter Notebook

Open `QuantumErrorVisualizer-demo.ipynb` for a complete walkthrough covering all modules with physics explanations and visualizations.
