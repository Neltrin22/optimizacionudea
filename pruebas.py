import sympy as sp

# Define una variable simbólica
x = sp.symbols('x')

# Define una función simbólica
f = x**2

# Calcula la derivada simbólica
derivada_simbolica = sp.diff(f, x)

# Imprime la derivada simbólica
print(f'Derivada: {derivada_simbolica}')

# Puedes evaluar la derivada en puntos específicos
x_valor = 2
resultado = derivada_simbolica.subs(x, x_valor)
print(f'Derivada en x={x_valor}: {resultado}')
