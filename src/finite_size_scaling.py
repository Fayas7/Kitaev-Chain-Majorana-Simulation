import numpy as np
import matplotlib.pyplot as plt

from hamiltonian import build_kitaev_chain

t =1.0
delta = 1.0
mu = 0.5

chain_lengths = [10, 20, 30, 40, 50, 75, 100]
min_energies = []

for N in chain_lengths:
    H = build_kitaev_chain(
        N=N,
        t=t,
        delta=delta,
        mu=mu
    )
    eigenvalues, _ = np.linalg.eigh(H)
    min_energy = np.min(np.abs(eigenvalues))
    min_energies.append(min_energy)

    print(
        f"Chain Length: {N}," 
        f"Minimum Absolute Energy: {min_energy:.8e}"
    )
plt.figure(figsize=(10,6))
plt.semilogy(
    chain_lengths,
    min_energies,
    marker='o',
    linestyle='-',
    color='blue'
)

plt.title("Finite Size Scaling of Majorana Energy Splitting")
plt.xlabel("Chain Length N")
plt.ylabel("Minimum Absolute Energy |E_min|")
plt.grid(True)

plt.savefig(
    "../results/finite_size_scaling.png",
    dpi=300,
    bbox_inches="tight"
)   

plt.show()

"""
Output:
Chain Length: 10,Minimum Absolute Energy: 1.78813934e-06
Chain Length: 20,Minimum Absolute Energy: 1.70468965e-12
Chain Length: 30,Minimum Absolute Energy: 4.80161738e-16
Chain Length: 40,Minimum Absolute Energy: 3.19528613e-17
Chain Length: 50,Minimum Absolute Energy: 1.62004061e-17
Chain Length: 75,Minimum Absolute Energy: 2.33271401e-16
Chain Length: 100,Minimum Absolute Energy: 3.47822515e-16
the fig is saved in ../results/finite_size_scaling.png
"""

"""
Stage 6: Finite Size Scaling Observation

The minimum absolute energy of the Kitaev chain was evaluated for several chain lengths while keeping the system within the topological phase (μ = 0.5, t = 1.0, Δ = 1.0).

The results show a rapid decrease in the energy splitting as the chain length increases. For N = 10, the minimum energy is approximately 1.8 × 10⁻⁶, while for N = 20 it decreases to approximately 1.7 × 10⁻¹². By N = 30, the minimum energy reaches values on the order of 10⁻¹⁶.

This behavior indicates that the overlap between Majorana modes located at opposite ends of the chain decreases rapidly with increasing system size. Consequently, the Majorana states become increasingly decoupled and approach exact zero-energy modes.

For larger chain lengths (N ≥ 30), the minimum energy reaches the numerical precision limit of double-precision floating-point arithmetic. The small fluctuations observed beyond this point are therefore attributed to numerical precision rather than physical effects.

These results provide strong evidence that the observed zero-energy states correspond to Majorana edge modes and demonstrate how topological protection improves as the chain length increases.


"""