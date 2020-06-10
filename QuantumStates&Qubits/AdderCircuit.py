from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit, execute, Aer
import matplotlib.pyplot as plt

# previous result circuit:
NumberQubits = 10
NumberOutputBits = 10
quantum_circuit = QuantumCircuit(NumberQubits, NumberOutputBits)

for ct in range(NumberOutputBits):
    quantum_circuit.measure(ct, ct)


# not gate flips 0 to 1 and 1 to 0
#  how to encode diff binary string as input

numberQBits = 10
qc = QuantumCircuit(numberQBits)
qc.x(9)
# applying the Pauli X gate (equivalent to NOT gate) on the qubit!

# print(qc.draw())

# can add 2 circuits together to also extract a result!
finalQC = qc + quantum_circuit
print(finalQC.draw())

# run this circuit and look at results!
res = execute(finalQC, Aer.get_backend('qasm_simulator')).result().get_counts()
plot_histogram(res)
plt.show()

# by flipping the leftmost bit ==> made the number 2^9 (because it's 100000000 in BINARY!)

#  CAN chain together these half adders (4 basic binary sums) to add anything!

# 1) Encode the 2 qubits, 2) Apply the algorithm, 3) Extract the 2 output bits @ the very end!
# dashed lines = barrier are used to distinguish diff parts of the cicuit, it can have other purposes also!

# for half sums ==> rightmost bit is 0 when both of the numbers are same and 1 when the numbers are diff
# job of XOR gate is done using Controlled-NOT gate ==> call it CNOT instead, which is abbrev as CX
# XOR gives true output (1) when the number of true (1) inputs is ODD

qc_CNOT = QuantumCircuit(2)
qc_CNOT.cx(0, 1)
print(qc_CNOT.draw())

# applied to 2 qubits, contro bit is small filled in square/circle and target = bigger circle/square with X
# writes over the target bit with the answer:  is 0 if BOTH inputs are 0 and 1 if diff
# example circuit using CNOT:

qc_CNOT = QuantumCircuit(2,2)
qc_CNOT.x(0)
qc_CNOT.cx(0,1)
qc_CNOT.measure(0, 0)
qc_CNOT.measure(1, 1)
qc_CNOT.draw(output = 'mpl')
plt.show()

qc_CNOT = QuantumCircuit(2,2)
qc_CNOT.cx(1, 0)
qc_CNOT.measure(0, 0)
qc_CNOT.measure(1, 1)
qc_CNOT.draw(output = 'mpl')
plt.show()


# can now create the half adder!
# simply need to use the CNOT operator on both qubits and write out the result!
# but because we don't want to override our original bits, we will be using more qubits
quantumAdder = QuantumCircuit(4, 2)
quantumAdder.x(0)
quantumAdder.x(1)
quantumAdder.barrier()
# onto the algorithm part!
quantumAdder.cx(0, 2)
quantumAdder.cx(1, 2)
quantumAdder.barrier()
# onto extracting the output now!
quantumAdder.measure(2, 0)
# write output of qubit 2 to bit 0 and output of qubit 3 to bit 1!
quantumAdder.measure(3, 1)
quantumAdder.draw(output = 'mpl')
# plt.show()

# we are still not there yet ==> 1 problem left, when adding 1 + 1, the quantum circuit using the CX gate will output 10
# but instead, we want it to output 11
# use Toffoli gate! ==> will perform the not gate on the target qubit (the one we're writing out to) when both inputs are 1
# Toffoli gate is similar to AND gate!

# use ccx command for Toffoli!
# FINAL QUANTUM ADDER CIRCUIT!
quantumAdder = QuantumCircuit(4, 2)
quantumAdder.x(0)
quantumAdder.x(1)
quantumAdder.barrier()
# onto the algorithm part!
quantumAdder.cx(0, 2)
quantumAdder.cx(1, 2)
quantumAdder.ccx(0, 1, 3)
quantumAdder.barrier()
# onto extracting the output now!
quantumAdder.measure(2, 0)
# write output of qubit 2 to bit 0 and output of qubit 3 to bit 1!
quantumAdder.measure(3, 1)
quantumAdder.draw(output = 'mpl')
plt.show()

res = execute(quantumAdder, Aer.get_backend('qasm_simulator')).result().get_counts()
plot_histogram(res)
plt.show()
