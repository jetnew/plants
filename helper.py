from turtle import *

# Configurations
pencolor("white")
bgcolor("black")
speed(0)
ht()
lt(90)
pu()
goto(0, -250)
pd()

def generate(axiom, rule, iterations):
  s = axiom
  for i in range(iterations):
    s = "".join(rule[c] for c in s)
  return s

states = []
def render(s, angle, length):
  for c in s:
    if c == 'F' or c == 'A':
      fd(length)
    elif c == '+':
      lt(angle)
    elif c == '-':
      rt(angle)
    elif c == '[':
      states.append((xcor(), ycor(), heading()))
    elif c == ']':
      x, y, head = states.pop()
      pu()
      goto(x, y)
      pd()
      setheading(head)


def create(axiom, rule, angle, length, iterations):
  result = generate(axiom, rule, iterations)
  print("Length:", len(result))
  render(result, angle, length)
