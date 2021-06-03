from sympy import *
import numpy as np


class LiczbyZespolone:
    def __init__(self, z):
        self.re = re(z)
        self.im = im(z)
        self.z = z
        self.modul = self.__modul()

    def __modul(self):
        modul = sqrt(self.re**2 + self.im**2)
        pprint(Eq(symbols('|z|'), modul))
        return modul

    def __kat_phi(self):
        phi = symbols('phi')
        modul = self.modul
        eq1 = Eq(cos(phi), self.re/modul)
        eq2 = Eq(sin(phi), self.im/modul)
        phi = solve([eq1, eq2], phi)[-1][-1]
        pprint(eq1)
        pprint(eq2)
        pprint(Eq(symbols('phi'), phi))
        return phi

    def postac_trygonometryczna(self, potega=None):
        phi = self.__kat_phi()
        modul = self.modul
        phi_symbol = symbols(f'{phi}')
        modul = self.modul
        eq = Eq(symbols('z'), modul * (cos(phi_symbol)+I*sin(phi_symbol)))
        pprint(eq)
        if potega:
            phi_symbol = symbols(f'{phi*potega}')
            eq = Eq(symbols(f'z^{potega}'), modul**potega * (cos(phi_symbol)+I*sin(phi_symbol)))
            pprint(eq)
            return eq 
        return eq

    def zbiory(self):
        pass
z = LiczbyZespolone(sqrt(3)+I)
z.postac_trygonometryczna(13)



