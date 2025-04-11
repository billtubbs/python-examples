"""Demonstration of multiple inheritance in Python with dataclasses."""

from dataclasses import dataclass


@dataclass
class Parent:
    A: int
    B: int

    def __init__(self, A, B):
        self.A = A
        self.B = B


class Child1(Parent):
    def __init__(self, *args, **kwargs):
        A = 1
        B = 2
        super().__init__(A, B, *args, **kwargs)


@dataclass
class Child2(Parent):
    Q: int
    R: int

    def __init__(self, A, B, Q, R):
        super().__init__(A, B)
        self.Q = Q
        self.R = R


class Hybrid(Child1, Child2):
    def __init__(self, Q, R):
        super().__init__(Q, R)
