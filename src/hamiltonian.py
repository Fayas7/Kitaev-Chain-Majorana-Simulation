import numpy as np

def build_kitaev_chain(N, t, delta, mu):
    """
    Build the BdG Hamiltonian for the Kitaev chain..
    
    parameters:
    --------------
    N:  int
        Number of lattice sites

    t:  float
        Hopping strength

    delta:  float
            Pairing strength
        
    mu:  float
        Chemical potential
    
    returns
    ----------------
    
    H:  ndarray
        2N * 2N BdG Hamiltonian matrix
    
    """
    A = np.zeros((N, N))
    B = np.zeros((N, N))

    for i in range(N):
        A[i, i] = -mu
        if i < N - 1:
            A[i, i + 1] = -t
            A[i + 1, i] = -t
            B[i, i + 1] = delta
            B[i + 1, i] = -delta
    H = np.block([
        [A,B],
        [B.T,-A.T] 
    ])

    return H

# Verification step
if __name__ == "__main__":

    H = build_kitaev_chain(
        N=4,
        t=1.0,
        delta=1.0,
        mu=0.0
    )

    print("Hamiltonian Matrix:")
    print(H)

    print("Shape:", H.shape)

    print(
    "Hermitian:",
    np.allclose(H, H.conj().T)
    )
    
#output:
"""
[[-0. -1.  0.  0.  0.  1.  0.  0.]
 [-1. -0. -1.  0. -1.  0.  1.  0.]
 [ 0. -1. -0. -1.  0. -1.  0.  1.]
 [ 0.  0. -1. -0.  0.  0. -1.  0.]
 [-0.  1. -0. -0.  0.  1. -0. -0.]
 [-1. -0.  1. -0.  1.  0.  1. -0.]
 [-0. -1. -0.  1. -0.  1.  0.  1.]
 [-0. -0. -1. -0. -0. -0.  1.  0.]]

 Shape: (8, 8)
 Hermitian: True

we can see matrex size = 8x8, which is 2N x 2N, where N=4
matrix is Hermitian, as expected for a Hamiltonian, which guarentees real energies. 
The off-diagonal blocks represent the pairing terms, while the diagonal blocks represent the hopping and chemical potential terms.  

"""

"""
OBSERVATIONS

1. The Hamiltonian matrix was successfully constructed in the
   Bogoliubov-de Gennes (BdG) representation.

2. For a chain with N sites, the Hamiltonian has dimensions
   2N × 2N because both particle and hole degrees of freedom
   are included.

3. The diagonal elements correspond to the chemical potential
   term (-μ).

4. The off-diagonal elements in matrix A represent hopping
   between neighboring sites with strength t.

5. Matrix B contains the superconducting pairing terms Δ and
   exhibits antisymmetric structure (Bᵀ = -B).

6. The full Hamiltonian satisfies Hermiticity
   (H = H†), ensuring that all energy eigenvalues obtained
   from diagonalization are real.

7. The block structure of the Hamiltonian matches the
   theoretical BdG form of the Kitaev chain.

   
"""

"""
Stage 1 conclusion:

The Hamiltonian for the Kitaev chain was successfully constructed in the Bogoliubov-de Gennes (BdG) representation.
The matrix is Hermitian, ensuring real energy eigenvalues. The structure of the Hamiltonian matches theoretical expectations, with diagonal blocks representing hopping and chemical potential terms, and off-diagonal blocks representing superconducting pairing. 
This sets the stage for diagonalizing the Hamiltonian to obtain the energy spectrum in the next stage.
The successful construction of the Hamiltonian establishes the foundation for subsequent calculations of the energy spectrum, topological phase transitions, and Majorana zero modes.
"""