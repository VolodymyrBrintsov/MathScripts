from sympy import *

class Popyt:
    def __init__(self, f, x, y):
        self.f = parse_expr(f)
        self.sym_x, self.sym_y = symbols('x y')
        self.x = x
        self.y = y
        self.f_x = self.f.diff('x')
        self.f_y = self.f.diff('y')

    def calculate_krancowosc(self):
        print(f'Jeżeli x zmieni się o jedną jednostkę a y nie zmieni się, y = {self.y} to popyt zwiększy się o '
              f'{self.f_x.subs([(self.sym_x, self.x), (self.sym_y, self.y)])}')
        print(
            f'Jeżeli y zmieni się o jedną jednostkę a x nie zmieni się, x = {self.x} to popyt zwiększy się o '
            f'{self.f_y.subs([(self.sym_x, self.x), (self.sym_y, self.y)])}')

    def calculate_elastycznosc(self):
        calculated_f = self.f.subs([(self.sym_x, self.x), (self.sym_y, self.y)])
        calculated_f_x = self.f_x.subs([(self.sym_x, self.x), (self.sym_y, self.y)])
        calculated_f_y = self.f_y.subs([(self.sym_x, self.x), (self.sym_y, self.y)])
        funkcja_elastycznosci = self.x/calculated_f * calculated_f_x
        print(f'Jeżeli x zmieni się o 1% z poziomu x = {self.x}, a y pozostanie na poziomie y = {self.y}, to popyt na y wzrośnie o {funkcja_elastycznosci}%')


p = Popyt('x*y*e**(12*x**2 -3*y**2)', 1, 2)
p.calculate_elastycznosc()