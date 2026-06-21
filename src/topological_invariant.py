import numpy as np
import matplotlib.pyplot as plt

t = 1.0
mu_values = np.linspace(-4, 4, 400)

invariant = []

for mu in mu_values:
    Q = np.sign(
        (mu + 2*t) *
        (mu - 2*t) 
    )
    invariant.append(Q)

invariant = np.array(invariant)

plt.figure(figsize=(10, 6))
plt.plot(mu_values, invariant, color='blue', linewidth=2)
plt.axvline(x=-2, color='red', linestyle='--', label='Critical Point: μ = -2')
plt.axvline(x=2, color='green', linestyle='--', label='Critical Point: μ = 2')
plt.title("Topological Invariant of the Kitaev Chain")
plt.xlabel("Chemical Potential μ")
plt.ylabel("Topological Invariant Q")
plt.grid(True)
plt.savefig(
    "../results/topological_invariant.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()



"""
## Stage 5: Topological Invariant Observation

The topological invariant Q of the Kitaev chain was evaluated as a function of the chemical potential μ for a system with hopping amplitude t = 1.0.

The invariant remains constant within each phase and changes abruptly at the critical values μ = -2 and μ = +2. For |μ| < 2, the invariant takes the value Q = -1, identifying the topological superconducting phase. For |μ| > 2, the invariant changes to Q = +1, corresponding to the trivial phase.

The locations of these transitions coincide exactly with the phase boundaries observed in the energy-spectrum calculations. Furthermore, the interval where Q = -1 matches the region in which Majorana zero modes and edge localization were observed.

The agreement between the topological invariant, energy spectrum, and localization analysis provides strong numerical evidence that the Kitaev chain undergoes a topological phase transition at μ = ±2t and supports Majorana zero modes only in the topological phase.


"""