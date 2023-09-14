import numpy as np
import pandas as pd
import sympy as sp

data = []  # Lista para almacenar los valores en cada iteración
tolerancia = 1e-6
x0 = 2.5
x = sp.symbols('x')
fx = 2 * sp.sin(x) - x**2 / 10


def df(f):
     derivada_simbolica = sp.diff(f, x)
     return derivada_simbolica


dx = df(fx)
d2x = df(dx)

def newton(xi):
    xi1 = xi - dx.subs(x, xi) / d2x.subs(x, xi)
    if abs(xi1 - xi) < tolerancia:
        return xi1
    else:
        return newton(xi1)
   

root = newton(x0)
    
    
print(f'Raíz encontrada: {root:.6f}')



