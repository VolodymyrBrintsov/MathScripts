from sympy import *

class EktremaLokalne:
    def __init__(self, function):
        self.function = parse_expr(function)
        self.function_x = self.function.diff('x')
        self.function_y = self.function.diff('y')
        self.x, self.y = symbols('x y')

    def get_punkts(self):
        eq1 = Eq(self.function_x, 0)
        eq2 = Eq(self.function_y, 0)
        critical_punkts = solve([eq1, eq2], [self.x, self.y])
        pprint(critical_punkts)
        return critical_punkts

    def make_hesse_matrix(self):
        function_xx = self.function_x.diff('x')
        function_xy = self.function_x.diff('y')
        function_yx = self.function_y.diff('x')
        function_yy = self.function_y.diff('y')
        hesse_matrix = Matrix([[function_xx, function_xy], [function_yx, function_yy]])
        pprint(hesse_matrix)
        return hesse_matrix

    def check_sufficien_condition(self):
        critical_punkts = self.get_punkts()
        hesse = self.make_hesse_matrix()
        for punkts in critical_punkts:
            x, y = punkts
            det_0 = hesse.row(0).col(0).det()
            det_1 = hesse.det()
            print(f'\nFor x = {x}, y = {y}:')
            H1 = det_0.subs([(self.x, x), (self.y, y)])
            H2 = det_1.subs([(self.x, x), (self.y, y)])
            pprint(Eq(symbols('H1'), H1))
            pprint(Eq(symbols('H2'), H2))
            if H1 > 0 and H2 > 0:
                print(f"P({x}, {y}) minimum lokalne")
            elif H1 < 0 and H2 > 0:
                print(f"P({x}, {y}) maksimum lokalne")
            else:
                print(f"P({x}, {y}) punkt siodlowy")

class EkstremaWarunkowe:
    def __init__(self, f, g):
        self.f = parse_expr(f)
        self.g = parse_expr(g)
        self.x, self.y, self.lambd = symbols('x y lambda')
        self.l = self.f + self.lambd * self.g
        self.l_x = self.l.diff('x')
        self.l_y = self.l.diff('y')

    def get_punkts(self):
        eq1 = Eq(self.l_x, 0)
        eq2 = Eq(self.l_y, 0)
        eq3 = Eq(self.g, 0)
        print('Do rozwiązania 3 równanania:\n')
        pprint(eq1)
        pprint(eq2)
        pprint(eq3)

        punkts = solve([eq1, eq2, eq3], [self.x, self.y, self.lambd])
        print(f'Mamy {len(punkts)} punkty:')
        for i, punkt in enumerate(punkts):
            x, y, lambd = punkt
            print(f'Punkt {i+1}({x}, {y}, {lambd})')
        return punkts

    def define_delta3(self):
        l_xx = self.l_x.diff('x')
        l_xy = self.l_x.diff('y')
        l_yx = self.l_y.diff('x')
        l_yy = self.l_y.diff('y')
        g_x = self.g.diff('x')
        g_y = self.g.diff('y')
        delta3_matrix = Matrix([[0, g_x, g_y], [g_x, l_xx, l_xy], [g_y, l_yx, l_yy]])
        pprint(delta3_matrix)
        delta3 = delta3_matrix.det()
        pprint(Eq(symbols('Delta3'), delta3))
        return delta3

    def check_sufficien_condition(self):
        critical_punkts = self.get_punkts()
        delta3 = self.define_delta3()
        for i, punkt in enumerate(critical_punkts):
            x, y, lambd = punkt
            print(f'Dla P({x}, {y}, {lambd}): ')
            delta_for_punkt = delta3.subs([(self.x, x), (self.y, y), (self.lambd, lambd)])
            pprint(Eq(symbols('Delta3'), delta_for_punkt))
            if delta_for_punkt > 0:
                print(f'P({x}, {y}, {lambd}) jest minimum lokalne')
            elif delta_for_punkt < 0:
                print(f'P({x}, {y}, {lambd}) maksimum lokalne')
            else:
                print(f'P({x}, {y}, {lambd}) punkt siodlowy')


EktremaLokalne('x**4 +y**4 -2*x**2 +4*x*y -2*y**2').check_sufficien_condition()

