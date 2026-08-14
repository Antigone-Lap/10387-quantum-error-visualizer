import qutip as qt

def fidelity_curve(rho0, states):
    return [qt.fidelity(rho0, s) for s in states]

def purity(rho):
    return (rho*rho).tr().real

def purity_curve(states):
    return [purity(s) for s in states]
