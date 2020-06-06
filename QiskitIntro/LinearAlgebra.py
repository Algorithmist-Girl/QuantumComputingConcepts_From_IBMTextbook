from qiskit import *
from matplotlib import pyplot as plt
import numpy as np
from qiskit.visualization import plot_bloch_vector

# creating a vector, which has BOTH magnitude and direction!
plt.figure()
ax = plt.gca()

ax.quiver([2], [4], angles = 'xy', scale_units = 'xy', scale = 2)

ax.set_xlim([0, 6])
ax.set_ylim([0, 6])

plt.draw()
plt.show()

#  quantum computing ==> uses state vectors ==> vectors that point to a specific point in space that
#  corr to a particular quantum state
#  use a bloch sphere to visualize this!

#  state space = all poss state vectors, or in other words all poss states that the vectors can point to!
plot_bloch_vector([1, 0, 0])
plt.show()
#  this state is a superposition between 0 & 1 bits

# vector is an element of the vector space
# vector space ==> 2 conditions, vector addition and scalar multiplication BOTH hold
#  given a vector v, if we operate vector addition or scalar multiplication on v, the resulting vector will also be in the
# same vector space!

# matrices ==> transform vectors into other vectors!

# quantum computation is performed by applying a matrix to a quantum state vector, which manipulates the vector!
# vector = matrix with 1 COLUMN
# manipulate qubits using quantum gates (quantum gates rep as matrices), which are applied to vectors, altering their states


# 2 impo types of matrices- Hermitian and Unitary!
# hermitian = conjugate transpose, means that if we flip the sign of the matrices imaginary components
# and then reflect the entires along main diagonal ==> it produes the SAME EQUAL MATRIX! (Ex- Pauli Y)

# Unitary matrix= inverse matrix = conjugate transpose of orig matrix!
# inverse * original = identity matrix

# concept- evolution of a quantum state by application of a unitary matrix PRESERVES the quantum state!
