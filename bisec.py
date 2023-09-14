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
        xr = (xl + xu) / 2
        fxr = f(xr)
        error = abs(xu - xr)
        #data.append([xu, xl, xr, fxl, fxu, fxr, fxl * fxr, error])
        
        if error <= tolerancia:
            df = pd.DataFrame(data, columns=["xu", "xl", "xr", "fxl", "fxu", "fxr", "fxl*fxr", "error"])
            return df, xr
        else:
            if fxl * fxr < 0:
                xu = xr
                data.append([xu, xl, xr, fxl, fxu, fxr, fxl * fxr, error])
                return bisec(xl, xu)  
            elif fxl * fxr > 0:
                xl = xr
                data.append([xu, xl, xr, fxl, fxu, fxr, fxl * fxr, error])
                return bisec(xl, xu)  
            else:
                #data.append([xu, xl, xr, fxl, fxu, fxr, fxl * fxr, error])
                return xr
    else:
        return "Elija otros valores"


root = bisec(xl, xu)
print(root)
