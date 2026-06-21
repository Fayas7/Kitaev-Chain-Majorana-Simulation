# Numerical Investigation of Majorana Zero Modes in the Kitaev Chain

**Author:** Fayas Muhammed

---

# Abstract

Majorana zero modes are exotic quasiparticle excitations that emerge in topological superconductors and are considered promising candidates for fault-tolerant quantum computation. The Kitaev chain provides one of the simplest theoretical models supporting Majorana edge states.

In this project, the Kitaev chain was investigated through numerical simulation using the Bogoliubov-de Gennes formalism. The Hamiltonian was constructed and diagonalized to study the energy spectrum, topological phase transitions, Majorana localization, topological invariants, and finite-size effects.

The numerical results demonstrate the emergence of Majorana zero modes within the topological phase, confirm the existence of a topological phase transition at the theoretically predicted critical points, and illustrate how topological protection improves with increasing system size.

---

# 1. Introduction

Topological phases of matter represent one of the most important developments in modern condensed matter physics. Unlike conventional phases that are characterized by symmetry breaking, topological phases are distinguished by global properties that remain robust against local perturbations.

One particularly important class of topological systems is topological superconductors, which can host Majorana zero modes at their boundaries.

Majorana modes possess non-Abelian exchange statistics and have attracted significant interest because of their potential applications in fault-tolerant quantum computation.

The Kitaev chain, introduced by Alexei Kitaev in 2001, is a one-dimensional p-wave superconducting model that provides a minimal theoretical framework for studying Majorana physics.

The objective of this project is to numerically investigate the Kitaev chain and reproduce its key topological properties.

---

# 2. Theoretical Background

## 2.1 Majorana Zero Modes

A Majorana fermion is a particle that is identical to its own antiparticle.

Although elementary Majorana particles have not yet been conclusively observed, Majorana quasiparticles can emerge as collective excitations in condensed matter systems.

These quasiparticles appear as zero-energy states localized at the boundaries of topological superconductors.

---

## 2.2 Kitaev Chain Model

The Kitaev chain Hamiltonian is

$$
H =
-\mu \sum_i c_i^\dagger c_i
-
t \sum_i
(c_i^\dagger c_{i+1}+h.c.)
+
\Delta \sum_i
(c_i c_{i+1}+h.c.)
$$

where:

- μ is the chemical potential
- t is the hopping amplitude
- Δ is the superconducting pairing strength

The model exhibits both trivial and topological superconducting phases depending on the value of μ.

---

## 2.3 Topological Phase Transition

The phase boundary occurs when

$$
|\mu| = 2t
$$

For

$$
|\mu| < 2t
$$

the system is topological and supports Majorana zero modes.

For

$$
|\mu| > 2t
$$

the system is topologically trivial.

---

# 3. Methodology

The project was divided into six stages:

### Stage 1: Hamiltonian Construction

The Bogoliubov-de Gennes Hamiltonian was implemented as a 2N × 2N matrix containing particle and hole sectors.

The Hamiltonian was verified to be Hermitian.

---

### Stage 2: Energy Spectrum Analysis

The Hamiltonian was diagonalized using exact numerical methods.

The resulting eigenvalues were analyzed to identify zero-energy states and particle-hole symmetry.

---

### Stage 3: Topological Phase Transition

The chemical potential was varied across a wide range.

Energy spectra were computed for each value of μ to identify the critical points separating the topological and trivial phases.

---

### Stage 4: Majorana Localization

The spatial probability distribution of the zero-energy eigenstate was calculated.

The localization profile was used to determine whether the mode resided at the chain boundaries.

---

### Stage 5: Topological Invariant

A topological invariant was evaluated as a function of μ and compared with the observed phase boundaries.

---

### Stage 6: Finite-Size Scaling

Chains of different lengths were simulated to investigate the energy splitting caused by overlap between edge Majorana modes.

---

# 4. Results

## 4.1 Energy Spectrum

The spectrum exhibited particle-hole symmetry and contained states extremely close to zero energy.

These states provided the first indication of Majorana zero modes.

---

## 4.2 Phase Transition

A topological phase transition was observed at

$$
\mu = \pm 2
$$

which agrees with theoretical predictions for

$$
t = 1
$$

The zero-energy states existed only within the topological region.

---

## 4.3 Majorana Localization

The zero-energy eigenstate was found to be strongly localized at the boundary of the chain.

This localization behavior is consistent with Majorana edge modes.

---

## 4.4 Topological Invariant

The invariant changed abruptly at the same critical values where the phase transition occurred.

The invariant correctly distinguished between topological and trivial phases.

---

## 4.5 Finite-Size Scaling

The energy splitting decreased rapidly as the chain length increased.

This behavior demonstrates the reduction of Majorana overlap and the emergence of topological protection.

---

# 5. Discussion

The numerical results obtained throughout this project are consistent with the theoretical predictions of the Kitaev chain model.

The agreement between:

- Energy spectrum calculations
- Phase-transition analysis
- Localization measurements
- Topological invariants
- Finite-size scaling

provides strong evidence for the existence of Majorana zero modes in the topological phase.

The project demonstrates how topology, rather than local symmetry breaking, determines the existence of protected boundary states.

---

# 6. Conclusion

This project successfully reproduced the key physical properties of the Kitaev chain through numerical simulation.

Majorana zero modes were identified through spectral analysis, localization measurements, and topological characterization.

The results illustrate fundamental concepts in topological superconductivity and provide a computational introduction to Majorana-based quantum information platforms.

Future work may include:

- Braiding simulations
- Kitaev ladder models
- Topological quantum gates
- Open quantum systems
- Quantum error correction using Majorana modes

---

# References

1. Kitaev, A. Y. (2001). Unpaired Majorana Fermions in Quantum Wires.
2. Alicea, J. (2012). New Directions in the Pursuit of Majorana Fermions in Solid State Systems.
3. Beenakker, C. W. J. (2013). Search for Majorana Fermions in Superconductors.
4. Nayak et al. (2008). Non-Abelian Anyons and Topological Quantum Computation.
5. Nielsen & Chuang. Quantum Computation and Quantum Information.
6. Bernevig & Hughes. Topological Insulators and Topological Superconductors.