from qiskit import *
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
from math import  pi
#gates = operations that changes qubits!

# Pauli gate!!
# multiply qubit's statevector by the gate to see the effect!!

# 1 qubit!!
quantum_circuit = QuantumCircuit(1)
quantum_circuit.x(0)
quantum_circuit.draw('mpl')
plt.show()

# plot_bloch_multivector takes in the qubit's statevector instead of the Bloch vector!!
backend = Aer.get_backend('statevector_simulator')
res= execute(quantum_circuit, backend).result().get_statevector()
plot_bloch_multivector(res)
plt.show()