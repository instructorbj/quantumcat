from enum import Enum


class OpType(Enum):
    """docstring for OpType."""

    x_gate = 1
    y_gate = 2
    z_gate = 3
    cx_gate = 4
    ccx_gate = 5
    mct_gate = 6
    measure = 100
