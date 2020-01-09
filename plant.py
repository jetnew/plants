from turtle import fd, lt, rt, xcor, ycor, heading, pu, pd, setheading, goto


class Plant:
    def __init__(self,
                 axiom,
                 rule,
                 angle,
                 length,
                 iterations):
        self.axiom = axiom
        self.rule = rule
        self.angle = angle
        self.length = length
        self.iterations = iterations

    def generate(self):
        self.pattern = self.axiom
        for _ in range(self.iterations):
            self.pattern = "".join(self.rule[c] for c in self.pattern)

    def render(self):
        states = []
        for c in self.pattern:
            if c == 'F' or c == 'A':
                fd(self.length)
            elif c == '+':
                lt(self.angle)
            elif c == '-':
                rt(self.angle)
            elif c == '[':
                states.append((xcor(), ycor(), heading()))
            elif c == ']':
                x, y, head = states.pop()
                pu()
                goto(x, y)
                pd()
                setheading(head)