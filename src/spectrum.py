import numpy as np
import matplotlib.pyplot as plt

from hamiltonian import build_kitaev_chain

# System parameters
N = 20 
t = 1.0
delta = 1.0
mu = 0.0

# Build the Kitaev chain Hamiltonian
H = build_kitaev_chain(
    N=N,
    t=t,
    delta=delta,
    mu = mu
)

#diagonalize the Hamiltonian
eigenvalues, eigenvectors = np.linalg.eigh(H)

#print energies
print("Eigenvalues:")
print(eigenvalues)

#plot the energy spectrum
plt.figure(figsize=(8, 5))

plt.plot(
    range(len(eigenvalues)),
    eigenvalues,
    marker='o'
)

plt.title("Energy Spectrum of the Kitaev Chain")
plt.xlabel("State Index")
plt.ylabel("Energy")
plt.grid(True)
plt.savefig(
    "../results/energy_spectrum.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print("\nLowest absolute energy:")
print(np.min(np.abs(eigenvalues)))

#output:
"""
Eigenvalues:
[-2.00000000e+00 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00
 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00
 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00
 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00
 -2.00000000e+00 -2.00000000e+00 -2.00000000e+00 -1.35395167e-15
  4.44089176e-16  2.00000000e+00  2.00000000e+00  2.00000000e+00
  2.00000000e+00  2.00000000e+00  2.00000000e+00  2.00000000e+00
  2.00000000e+00  2.00000000e+00  2.00000000e+00  2.00000000e+00
  2.00000000e+00  2.00000000e+00  2.00000000e+00  2.00000000e+00
  2.00000000e+00  2.00000000e+00  2.00000000e+00  2.00000000e+00]

Lowest absolute energy:
4.4408917631518795e-16
energy_spectrum.png is saved in results folder

"""


"""
OBSERVATIONS

1. The energy spectrum is symmetric about E = 0.
2. This symmetry arises from particle-hole symmetry in the BdG Hamiltonian.
3. For μ = 0, t = 1, and Δ = 1, the system is in the topological regime.
4. Near-zero-energy states may indicate Majorana edge modes.
5. Increasing chain length should reduce finite-size splitting.
"""
"""
## Stage 2 Conclusion:

The energy spectrum of the Kitaev chain was obtained by diagonalizing the Bogoliubov-de Gennes Hamiltonian for a chain of N = 20 sites with parameters t = 1.0, Δ = 1.0, and μ = 0.0.
The calculated spectrum exhibits particle-hole symmetry, with positive and negative energy states appearing in symmetric pairs. This behavior is expected for superconducting systems described by the BdG formalism.
Two eigenvalues were found extremely close to zero energy, with the minimum absolute energy equal to approximately 4.44 × 10⁻¹⁶. This value is effectively zero within numerical precision and indicates the presence of zero-energy modes.
The large degeneracy observed at energies ±2 is a consequence of the highly symmetric parameter choice (t = Δ and μ = 0), often referred to as the special or ideal point of the Kitaev chain. At this point, Majorana modes are expected to be perfectly localized at the ends of the chain.
These results provide the first numerical evidence of the topological phase and the emergence of Majorana zero modes in the model.

"""