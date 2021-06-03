from sympy import *

class Popyt:
    def __init__(self, f, x, y):
        self.f = parse_expr(f)
        self.sym_x, self.sym_y = symbols('x y')
        self.x = x
        self.y = y

    def calculate_krancowosc(self):
        f_x = self.f.diff('x')
        f_y = self.f.diff('y')
        print(f'Jeżeli x zmieni się o jedną jednostkę a y nie zmieni się, y = {self.y} to popyt zwiększy się o {f_x.subs([(self.sym_x, self.x), (self.sym_y, self.y)])}')
        print(
            f'Jeżeli y zmieni się o jedną jednostkę a x nie zmieni się, x = {self.x} to popyt zwiększy się o {f_y.subs([(self.sym_x, self.x), (self.sym_y, self.y)])}')

p = Popyt('1200*x +500*y +x**2*y - x**3 - y**2', 30, 60)
p.calculate_krancowosc()