from quantumcat.circuit.op_type import OpType
from qiskit.circuit.library import standard_gates
from cirq import ops

quantumcat_to_qiskit = {
    OpType.x_gate: standard_gates.x.XGate,
    OpType.y_gate: standard_gates.y.YGate,
    OpType.z_gate: standard_gates.z.ZGate,
    OpType.cx_gate: standard_gates.x.CXGate,
    OpType.measure: OpType.measure,
}

quantumcat_to_cirq = {
    OpType.x_gate: ops.pauli_gates.X,
    OpType.y_gate: ops.pauli_gates.Y,
    OpType.z_gate: ops.pauli_gates.Z,
    OpType.cx_gate: ops.common_gates.CNOT,
    OpType.measure: OpType.measure,
}
