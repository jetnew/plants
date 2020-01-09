from plant import Plant
from util import initialise

initialise()

axial_tree = Plant(axiom='X',
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
                   iterations=5)
axial_tree.generate()
axial_tree.render()

plant_a = Plant(axiom='F',
                rule={
                    'F': 'F[+F]F[-F]F',
                    '+': '+',
                    '-': '-',
                    '[': '[',
                    ']': ']',
                },
                angle=25.7,
                length=2,
                iterations=5)
plant_a.generate()
plant_a.render()

plant_b = Plant(axiom='F',
                rule={
                    'F': 'F[+F]F[-F][F]',
                    '+': '+',
                    '-': '-',
                    '[': '[',
                    ']': ']',
                },
                angle=20,
                length=8,
                iterations=5)
plant_b.generate()
plant_b.render()

plant_c = Plant(axiom='F',
                rule={
                    'F': 'FF-[-F+F+F]+[+F-F-F]',
                    '+': '+',
                    '-': '-',
                    '[': '[',
                    ']': ']',
                },
                angle=22.5,
                length=8,
                iterations=4)
plant_c.generate()
plant_c.render()

plant_d = Plant(axiom='X',
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
                iterations=7)
plant_d.generate()
plant_d.render()

plant_e = Plant(axiom='X',
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
                iterations=7)
plant_e.generate()
plant_e.render()

plant_f = Plant(axiom='X',
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
                iterations=5)
plant_f.generate()
plant_f.render()

done()