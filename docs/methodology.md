# Methodology

## Overview

This project investigates Majorana zero modes and topological superconductivity in the Kitaev chain through numerical simulation.

The study was performed in several stages:

1. Hamiltonian Construction
2. Energy Spectrum Analysis
3. Phase Transition Analysis
4. Majorana Localization Analysis
5. Topological Invariant Calculation
6. Finite-Size Scaling Analysis

---

## Hamiltonian Construction

The Kitaev chain was implemented using the Bogoliubov-de Gennes (BdG) formalism.

For a chain containing N lattice sites, the Hamiltonian was represented as a 2N × 2N matrix containing both particle and hole degrees of freedom.

The Hamiltonian was constructed using:

- Chemical potential (μ)
- Hopping amplitude (t)
- Pairing amplitude (Δ)

The matrix was verified to be Hermitian before proceeding with spectral calculations.

---

## Energy Spectrum Analysis

The Hamiltonian was diagonalized using

```python
numpy.linalg.eigh()
```

which is optimized for Hermitian matrices.

The eigenvalues correspond to the allowed energy levels of the system.

The energy spectrum was analyzed to identify:

- Particle-hole symmetry
- Energy gaps
- Near-zero-energy states

---

## Phase Transition Analysis

The chemical potential μ was varied over the interval

$$
-4 \leq \mu \leq 4
$$

For each value of μ:

1. The Hamiltonian was constructed.
2. The spectrum was computed.
3. All eigenvalues were stored.

The resulting energy bands were plotted as a function of μ to identify the phase boundaries.

---

## Majorana Localization Analysis

The eigenstate corresponding to the energy closest to zero was extracted.

The probability density was computed using both particle and hole components:

$$
P_i =
|u_i|^2
+
|v_i|^2
$$

where:

- $u_i$ represents the particle component
- $v_i$ represents the hole component

The probability density was plotted across all lattice sites to determine whether the state was localized at the edges.

---

## Topological Invariant Calculation

The topological invariant was calculated using

$$
Q =
\text{sign}
\left[
(\mu + 2t)
(\mu - 2t)
\right]
$$

The invariant was evaluated across a range of chemical potentials and compared with the phase boundaries observed in the spectral calculations.

---

## Finite-Size Scaling Analysis

Chains of varying length were simulated:

- N = 10
- N = 20
- N = 30
- N = 40
- N = 50
- N = 75
- N = 100

For each chain length, the minimum absolute energy was extracted.

The scaling behavior of the energy splitting was used to investigate the overlap between Majorana modes located at opposite ends of the chain.

---

## Computational Tools

The simulations were implemented in Python using:

- NumPy
- Matplotlib
- Jupyter Notebook

All calculations were performed using exact diagonalization of the BdG Hamiltonian.