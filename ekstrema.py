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

EktremaLokalne('x**3 +3*x*y**2 +6*x*y').check_sufficien_condition()