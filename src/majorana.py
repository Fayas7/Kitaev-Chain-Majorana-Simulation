import numpy as np
import matplotlib.pyplot as plt

from hamiltonian import build_kitaev_chain

#parameters
N = 20
t = 1.0
delta = 1.0
mu = 0.0

# build the Kitaev chain Hamiltonian
H = build_kitaev_chain(
    N=N,
    t=t,
    delta=delta,
    mu=mu
)

#diagonalize the Hamiltonian
eigenvalues, eigenvectors = np.linalg.eigh(H)

#find state closest to zero energy
zero_mode_index = np.argmin(np.abs(eigenvalues))
print("closest energy:")
print(eigenvalues[zero_mode_index])

#corresponding eigenvector
zero_mode = eigenvectors[:, zero_mode_index]

# Probability on each physical site

particle_part = zero_mode[:N]
hole_part = zero_mode[N:]

probability = (
    np.abs(particle_part)**2 +
    np.abs(hole_part)**2
)

print("Probability before normalization:")
print(probability)

print("Sum before normalization:")
print(np.sum(probability))

# Normalize
probability = probability / np.sum(probability)

print("\nProbability after normalization:")
print(probability)

print("Sum after normalization:")
print(np.sum(probability))

#plot 
sites = np.arange(1,N+1)
plt.figure(figsize=(10, 5))
plt.plot(
    sites,
    probability,
    marker='o',
    color='purple'
)
plt.xlabel("Site Index")
plt.ylabel("Probability Density")
plt.title("Majorana Zero Mode Localization")

plt.grid(True)

plt.savefig(
    "../results/majorana_localization.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

"""
output:
closest energy:
4.4408917631518795e-16
Probability before normalization:
[2.16073065e-69 0.00000000e+00 8.97546372e-38 6.19754167e-33
 8.68882964e-37 7.16814747e-33 8.04478489e-34 6.95107099e-33
 8.08696560e-34 1.15181147e-32 4.73484403e-33 3.77687608e-32
 3.02459032e-33 6.29892227e-32 2.28619563e-33 2.98279974e-32
 2.98991078e-33 2.22210520e-33 2.04651347e-33 1.00000000e+00]
Sum before normalization:
1.0000000000000007

Probability after normalization:
[2.16073065e-69 0.00000000e+00 8.97546372e-38 6.19754167e-33
 8.68882964e-37 7.16814747e-33 8.04478489e-34 6.95107099e-33
 8.08696560e-34 1.15181147e-32 4.73484403e-33 3.77687608e-32
 3.02459032e-33 6.29892227e-32 2.28619563e-33 2.98279974e-32
 2.98991078e-33 2.22210520e-33 2.04651347e-33 1.00000000e+00]
Sum after normalization:
1.0
the fig is saved in results folder as majorana_localization.png
"""

"""
Stage 4 Observations:

The zero-energy eigenstate of the Kitaev chain was analyzed for a system with N = 20 sites, hopping amplitude t = 1.0, pairing strength Δ = 1.0, and chemical potential μ = 0.0.
The closest energy to zero was found to be approximately 4.44e-16, effectively zero within numerical precision, confirming the presence of a Majorana zero mode.
The probability density of the zero mode was computed and normalized, revealing a strong localization at the last site of the chain (site index 20) with a probability density of 1.0, while the other sites have negligible probability densities on the order of 10^-33 or smaller.
This localization behavior is a characteristic signature of a Majorana edge mode. The result confirms that the zero-energy states identified in the energy spectrum are not bulk states but boundary states associated with the topological superconducting phase.
The observed localization is particularly sharp because the chosen parameters correspond to the special point μ = 0 and t = Δ, where Majorana modes become perfectly localized at the chain ends. This result provides direct numerical evidence for the existence of Majorana zero modes in the Kitaev chain model.

"""