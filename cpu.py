from stack import Stack
from opcodes import *
from arithmetic import *
from push import _push
from comp import *
from logic import *
from bit import *
from env import *


class CPU:
    def __init__(self):
        self.pc = 0
        self.stack = Stack()
        self.program = []

    def load(self, program):
        self.reset()
        self.program = program

    def reset(self):
        self.pc, self.stack = 0, Stack()

    def peek(self, i=1):
        return self.program[self.pc + i]

    def run(self):
        op = self.program[self.pc]

        while op != STOP:
            # ARITHMETIC
            if op == ADD:    add(self)
            if op == MUL:    mul(self)
            if op == SUB:    sub(self)
            if op == DIV:    div(self)
            if op == SDIV:   sdiv(self)
            if op == MOD:    mod(self)
            if op == SMOD:   smod(self)
            if op == ADDMOD: addmod(self)
            if op == EXP:    exp(self)

            # COMP
            if op == LT:     lt(self)
            if op == GT:     gt(self)
            if op == EQ:     eq(self)
            if op == ISZERO: iszero(self)

            # LOGIC
            if op == AND: _and(self)
            if op == OR:  _or(self)
            if op == XOR: _xor(self)
            if op == NOT: _not(self)

            # BIT
            if op == SHL: shl(self)
            if op == SHR: shr(self)

            # ENV
            if op == ADDRESS: address(self)

            # PUSH
            if op == PUSH1:   _push(self, 1)
            if op == PUSH2:   _push(self, 2)
            if op == PUSH3:   _push(self, 3)
            if op == PUSH4:   _push(self, 4)
            if op == PUSH5:   _push(self, 5)
            if op == PUSH6:   _push(self, 6)
            if op == PUSH7:   _push(self, 7)
            if op == PUSH8:   _push(self, 8)
            if op == PUSH9:   _push(self, 9)
            if op == PUSH10:  _push(self, 10)
            if op == PUSH11:  _push(self, 11)
            if op == PUSH12:  _push(self, 12)
            if op == PUSH13:  _push(self, 13)
            if op == PUSH14:  _push(self, 14)
            if op == PUSH15:  _push(self, 15)
            if op == PUSH16:  _push(self, 16)
            if op == PUSH17:  _push(self, 17)
            if op == PUSH18:  _push(self, 18)
            if op == PUSH19:  _push(self, 19)
            if op == PUSH20:  _push(self, 20)
            if op == PUSH21:  _push(self, 21)
            if op == PUSH22:  _push(self, 22)
            if op == PUSH23:  _push(self, 23)
            if op == PUSH24:  _push(self, 24)
            if op == PUSH25:  _push(self, 25)
            if op == PUSH26:  _push(self, 26)
            if op == PUSH27:  _push(self, 27)
            if op == PUSH28:  _push(self, 28)
            if op == PUSH29:  _push(self, 29)
            if op == PUSH30:  _push(self, 30)
            if op == PUSH31:  _push(self, 31)
            if op == PUSH32:  _push(self, 32)

            op = self.program[self.pc]