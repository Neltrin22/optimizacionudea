import numpy as np

x0 = 0.0
x1 = 1.0
x2 = 4.0
tolerance = 1e-6  
max_iterations = 50

def f(x):
    return 2 * np.sin(x) - x**2 / 10

def quadratic_interpolation(x0, x1, x2):
    fx0, fx1, fx2 = f(x0), f(x1), f(x2)
    numerator = fx0 * (x1**2 - x2**2) + fx1 * (x2**2 - x0**2) + fx2 * (x0**2 - x1**2)
    denominator = 2 * (fx0 * (x1 - x2) + fx1 * (x2 - x0) + fx2 * (x0 - x1))

    if denominator == 0:
        return None  

    x3 = numerator / denominator
    if fx3 > fx1 & x3 > x1:
        x0 = x1
        x1 = x3
    else:
        x2 = x3
    return x3

print("Iteración\t  x0\t  x1\t  x2\t  x3\t  f(x3)")

for iteration in range(max_iterations):
    x3 = quadratic_interpolation(x0, x1, x2)

    if x3 is None:
        break

    fx3 = f(x3)


    print(f"{iteration + 1}\t  {x0:.4f}\t  {x1:.4f}\t  {x2:.4f}\t  {x3:.4f}\t  {fx3:.4f}")

    if abs(fx3) < tolerance:
        break

  
    


print("\nResultado final:")
print(f"x_optimal = {x3:.6f}")
print(f"f(x_optimal) = {fx3:.6f}")
