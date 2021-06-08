from sympy import *

class LiczbyZespolone:
    def __init__(self, z):
        self.re = re(z)
        self.im = im(z)
        self.z = z
        self.modul = self.__modul()
        self.phi = self.__angle_phi()

    def __modul(self):
        modul = sqrt(self.re**2 + self.im**2)
        print('Modul liczby jest równy:')
        pprint(Eq(symbols('|z|'), modul))
        return modul

    def __angle_phi(self):
        phi = symbols('phi')
        modul = self.modul
        sin_eq = Eq(cos(phi), self.re/modul)
        cos_eq = Eq(sin(phi), self.im/modul)
        phi = solve([sin_eq, cos_eq], phi)[-1][-1]
        print('\nŻeby znałeść kąt phi potrzebujemy roziązać dwa równania:')
        pprint(sin_eq)
        pprint(cos_eq)
        print('\nKąt phi:')
        pprint(Eq(symbols('phi'), phi))
        return phi

    def trigonometric_form(self):
        phi = self.phi
        phi_symbol = symbols(f'{phi}')
        modul = self.modul
        print('Postać trygonometryczna tej liczby:')
        eq = Eq(symbols('z'), modul * (cos(phi_symbol)+I*sin(phi_symbol)))
        pprint(eq)
        return eq

    @staticmethod
    def quadratic_eq():
        a, b, c = [parse_expr(i) for i in input('Wpisz a, b, c twojego równania kwadratowego:\n').split(' ')]
        symbol_delta, symbol_z, x, y = symbols('Delta z x y')

        print('\nTwoje równanie:')
        pprint(Eq(a * symbol_z**2 + b* symbol_z + c, 0))

        print('\nDelta jest równa:')
        delta_eq = Eq(symbol_delta, b**2 - 4*a*c)
        delta = solve(delta_eq)[0]
        pprint(delta_eq)
        pprint(Eq(symbol_delta, delta))

        delta_re, delta_im = re(delta), im(delta)
        delta_modul = sqrt(delta_re**2 + delta_im**2)

        print('\nMamy tzy równania:')
        eq1 = Eq(x ** 2 - y ** 2, delta_re)
        eq2 = Eq(2 * x * y, delta_im)
        eq3 = Eq(x ** 2 + y ** 2, delta_modul)
        pprint(eq1)
        pprint(eq2)
        pprint(eq3)

        print('\nZnależliśmy pierwiastek delty')
        x_and_y = solve([eq1, eq2, eq3], (x, y))
        fisrt_root = x_and_y[0][0] + x_and_y[0][1]*I
        second_root = x_and_y[1][0] + x_and_y[1][1]*I
        pprint(Eq(sqrt(symbol_delta), fisrt_root))
        pprint(Eq(sqrt(symbol_delta), second_root))

        print('\nKorzenie równania to:')
        z_1_symbol, z_2_symbol = symbols('z1 z2')
        z_1_eq = Eq(z_1_symbol, (-b + fisrt_root)/2*a)
        z_2_eq = Eq(z_2_symbol, (-b + second_root)/2*a)
        pprint(z_1_eq)
        pprint(z_2_eq)

    def __add__(self, other):
        self_eq = self.re + self.im*I
        other_eq = other.re + other.im*I
        sum = self_eq + other_eq
        z1, z2 = symbols('z1 z2')
        pprint(Eq(z1+z2, sum))
        return sum

    def __sub__(self, other):
        self_eq = self.re + self.im*I
        other_eq = other.re + other.im*I
        sub = self_eq - other_eq
        z1, z2 = symbols('z1 z2')
        pprint(Eq(z1-z2, sub))
        return sub

    def __mul__(self, other):
        self_eq = self.re + self.im*I
        other_eq = other.re + other.im*I
        z1, z2 = symbols('z1 z2')
        pprint(Eq(z1*z2, self_eq*other_eq))
        mul = re(self_eq)*re(other_eq)+re(self_eq)*im(other_eq)*I+im(self_eq)*I*re(other_eq)+im(self_eq)*I*im(other_eq)*I
        pprint(Eq(z1*z2, mul))
        return mul

    def __truediv__(self, other):
        self_eq = self.re + self.im * I
        other_eq = other.re + other.im * I
        z1, z2 = symbols('z1 z2')
        pprint(Eq(z1 / z2, self_eq / other_eq))
        return self_eq / other_eq

    def __pow__(self, power):
        modul_pow = pow(self.modul, power)
        phi = self.phi*power
        symbol_z_power, symbol_phi = symbols(f"z^{power} {phi}")
        z_power = modul_pow * (cos(phi) + I * sin(phi))
        eq1 = Eq(symbol_z_power, modul_pow * (cos(symbol_phi)+I*sin(symbol_phi)))
        eq2 = Eq(symbol_z_power, z_power)
        pprint(eq1)
        pprint(eq2)
        return z_power

    def zbiory(self, pot):
        res = 0
        phi = self.phi
        phi_symbol = symbols(f'{phi}')

        modul=self.modul
        modul_symbol=symbols(f'{modul}')

        pot_symbol = symbols(f'{pot}')
        for i in range (0, pot):
            res = (modul_symbol**(1/pot_symbol))*(cos((self.phi+2*i*pi)/pot)+I*sin((self.phi+2*i*pi)/pot))
            pprint(res)

x = symbols ('x', real=True)
z = LiczbyZespolone(-4*I)
z.zbiory(3)
