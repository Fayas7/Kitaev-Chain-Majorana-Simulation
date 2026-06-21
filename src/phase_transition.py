import numpy as np
import matplotlib.pyplot as plt

from hamiltonian import build_kitaev_chain

#parameters for the Kitaev chain
N = 20
t = 1.0
delta = 1.0

# Define a range of chemical potential values to explore the phase transition
mu_values = np.linspace(-4,4, 200)

all_energies = []

for mu in mu_values:
    H = build_kitaev_chain(
        N= N,
        t= t,
        delta= delta,
        mu= mu
    )
    eigenvalues, _ = np.linalg.eigh(H)
    all_energies.append(eigenvalues)

all_energies = np.array(all_energies)

plt.figure(figsize=(10, 6))

for band in range(all_energies.shape[1]):
    plt.plot(mu_values, all_energies[:, band], color='blue', linewidth=0.8)

#mark critical points
plt.axvline(x=-2, color='red', linestyle='--', label='Critical Point: μ = -2')
plt.axvline(x=2, color='green', linestyle='--', label='Critical Point: μ = 2')

plt.title("Kitaev Chain Phase Transition")
plt.xlabel("Chemical Potential μ")
plt.ylabel("Energy")    

plt.grid(True)

plt.savefig(
    "../results/phase_transition.png",
    dpi=300,
    bbox_inches="tight" 
)

plt.show()

"""
Stage 3 Observations:
## Stage 3: Topological Phase Transition Observation

The energy spectrum of the Kitaev chain was computed as a function of the chemical potential μ over the range -4 ≤ μ ≤ 4 for a chain with N = 20 sites, hopping amplitude t = 1.0, and pairing strength Δ = 1.0.

The resulting spectrum exhibits clear particle-hole symmetry, with positive and negative energy branches appearing as mirror images about E = 0. A pair of zero-energy states is observed throughout the interval -2 < μ < 2, forming a nearly flat band at zero energy.

The zero-energy modes disappear at μ = -2 and μ = +2, which coincide with the theoretical phase boundaries predicted by the Kitaev chain model. Near these critical values, the bulk energy bands approach the zero-energy states, indicating a closing of the energy gap.

The persistence of zero-energy modes within the interval -2 < μ < 2 provides numerical evidence for the topological superconducting phase and the existence of Majorana edge states. Outside this interval, the system transitions into the trivial phase, where the zero-energy modes are absent.

Overall, the numerical results are in excellent agreement with the theoretical prediction that the Kitaev chain undergoes a topological phase transition at μ = ±2t.


"""