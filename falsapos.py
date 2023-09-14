import numpy as np
import pandas as pd

tolerancia = 1e-6
xl = -10
xu = 20
data = []  # Lista para almacenar los valores en cada iteración
def f(x):
    return 3*x**2 - 120*x + 100

def bisec(xl, xu):
    
    fxl = f(xl)
    fxu = f(xu)

    if fxl * fxu < 0:
        xr = xu - ((fxu*(xl - xu)) / (fxl-fxu))
        fxr = f(xr)
        error = abs(xu - xr)
        #data.append([xu, xl, xr, fxl, fxu, fxr, fxl * fxr, error])
        
        if error <= tolerancia:
            df = pd.DataFrame(data, columns=["xu", "xl", "xr", "fxl", "fxu", "fxr", "error"])
            return df
        else:
            if abs(xl-xr) < abs(xr-xu):
                xl = xr
                data.append([xu, xl, xr, fxl, fxu, fxr, error])
                return bisec(xl, xu)  
            elif abs(xu-xr) < abs(xr-xl):
                xu = xr
                data.append([xu, xl, xr, fxl, fxu, fxr, error])
                return bisec(xl, xu)  
            else:
                #data.append([xu, xl, xr, fxl, fxu, fxr, fxl * fxr, error])
                return xr
    else:
        return "Elija otros valores"


root = bisec(xl, xu)
print(root)
