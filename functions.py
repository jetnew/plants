from helper import *


def axial_tree(n=5):
    create(axiom='X',
           rule={
               'X': 'F[-X][+X]',
               'F': 'F',
               '+': '+',
               '-': '-',
               '[': '[',
               ']': ']',
           },
           angle=30,
           length=100,
           iterations=n)


def plant_a(n=5):
    create(axiom='F',
           rule={
             'F': 'F[+F]F[-F]F',
             '+': '+',
             '-': '-',
             '[': '[',
             ']': ']',
           },
           angle=25.7,
           length=2,
           iterations=n)


def plant_b(n=5):
    create(axiom='F',
           rule={
             'F': 'F[+F]F[-F][F]',
             '+': '+',
             '-': '-',
             '[': '[',
             ']': ']',
           },
           angle=20,
           length=8,
           iterations=n)


def plant_c(n=4):
    create(axiom='F',
           rule={
             'F': 'FF-[-F+F+F]+[+F-F-F]',
             '+': '+',
             '-': '-',
             '[': '[',
             ']': ']',
           },
           angle=22.5,
           length=8,
           iterations=n)


def plant_d(n=7):
    create(axiom='X',
           rule={
             'X': 'F[+X]F[-X]+X',
             'F': 'FF',
             '+': '+',
             '-': '-',
             '[': '[',
             ']': ']',
           },
           angle=20,
           length=2,
           iterations=n)


def plant_e(n=7):
    create(axiom='X',
           rule={
             'X': 'F[+X][-X]FX',
             'F': 'FF',
             '+': '+',
             '-': '-',
             '[': '[',
             ']': ']',
           },
           angle=25.7,
           length=2,
           iterations=n)


def plant_f(n=5):
    create(axiom='X',
           rule={
             'X': 'F-[[X]+X]+F[+FX]-X',
             'F': 'FF',
             '+': '+',
             '-': '-',
             '[': '[',
             ']': ']',
           },
           angle=22.5,
           length=5,
           iterations=n)