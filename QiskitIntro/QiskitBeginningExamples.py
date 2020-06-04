# import mpmath
# import sympy

from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# import numpy as np

# currently empty with no qubits and no outputs!!
qc = QuantumCircuit()

# quantum register= system comprising of multiple qubits
# register of 2 qubits and qreg name is OPTIONAL
qr = QuantumRegister(2, 'qreg')

# to add this quantum register to the circuit, use add_register
qc.add_register(qr)

# check that this register has been added by printing out the regs (registers)
print(qc.qregs)

# to see what the circuit looks like (ONLY 2 QUBITS ==> CAN DRAW IT), sitting in state |0>
print(qc.draw())
# qc.draw(output='mpl')

# TO MAKE SOMETHING HAPPEN, NEED TO ADD GATES and apply to them to quibit(s)!!
qc.h(qr[0])
qc.h(qr[1])
# qc.cx(qr[0], qr[1])

# output of circuit after adding the gates!!
print(qc.draw())


# At the stage where we can actually look at the output of the circuit ==> USE Statevector simulator!
# statevector simulator ==> see what's happening to the statevectors of the 2 qubits
vector_sim = Aer.get_backend('statevector_simulator')

#backend ==> referring to things on which computer programs ARE ACTUALLY RUN ON (simulators or real quantum
# devices

# need to setup actual backend object, simulator we want is part of Aer
# get_backend() method of Aer  ==> get the backend object we need, name is 'statevector_simjulator'

#list of all poss backends located in Aer
print(Aer.backends())

# all of these poss backends are local meaning that they can be run on any local machine which has installed
# qiskit instead of connecting to cloud and having IBM Q account!
# running on simulation - done with execute method
job = execute(qc, vector_sim)

# stores object that is the result of the execute method, or the simulation using the execute method
# All that is left is TO EXTRACT THE RESULT ITSELF!!
#SPECICIALLY, WE WANT THE STATE vector of the qubits!!!
# NOW, printed out all of the states
ket = job.result().get_statevector()
for amplitude in ket:
    print(amplitude)






# in previous simulation, got out a statevector, but from real quantum computer, we get measurement
# this is done with ClassicalRegister, which measures both of our 2 qubits
cr = ClassicalRegister(2, 'creg')
qc.add_register(cr)

# add the measure method of the quantum circuit
# 2 args: the qubit being measured and the bit where the result is written
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])
print(qc.draw())

# can now run on a local simulator to emulate a real quantum device
# need to add another input to the emulate function ==> number of shots, how many times we run the circuit to take stats
# default val of shots = 1024 if you don't provide anything
emulator = Aer.get_backend('qasm_simulator')
job = execute(qc, emulator, shots=8192)

#result of job is a histogram in the form of a Python dictionary
hist = job.result().get_counts()
print(hist)

# can get qiskit to plot it as a histogram
# , color='midnightblue', title="New Histogram"

plot_histogram(data=job.result().get_counts())
plt.show()


# can also get the ordered list of results for the states of the 2 qubits when running the simulator
# bits are labeled from R to L, so cr[0] is furthest to the right
job = execute(qc, emulator, shots = 10, memory = True)
samples = job.result().get_memory()
print(samples)


# can also use simplifed notation if we don't need too many features
qc = QuantumCircuit(3)
# this means that this quant circ has 3 qubits, single quantum register containing 3 qubits
# AND, it also has NO classical register!
print(qc)

qc.h(2)
print(qc.draw())


# to have a circuit with BOTH quantum & classical registers ==> supply 2 arguments to QuantumCircuit
# # qubits, #classical bits
qc = QuantumCircuit(2, 1)
qc.h(0)
qc.cx(0,1)
qc.measure(1,0)
print(qc.draw())

# accessing on REAL QUANTUM HARDWARE!, NEED IBMQ acct
# IBMQ.load_account()