from helper import *


def koch_snowflake():
    create(axiom='F++F++F',
           rule={
               'F': 'F-F++F-F',
               '+': '+',
               '-': '-',
           },
           angle=60,
           length=5,
           iterations=4)


def dragon_curve():
    create(axiom='FX',
           rule={
               'Y': '-FX-Y',
               'X': 'X+YF+',
               '+': '+',
               '-': '-',
               'F': 'F',
           },
           angle=90,
           length=5,
           iterations=10)


def sierpinski_triangle():
    create(axiom='A',
           rule={
               'B': '-A+B+A-',
               'A': '+B-A-B+',
               '+': '+',
               '-': '-',
           },
           angle=60,
           length=3,
           iterations=7)