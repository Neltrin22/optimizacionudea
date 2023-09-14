import numpy as np
import pandas as pd

tolerancia = 1e-6
xl = 0
xu = 4

#b = 0.618*0.618*xu - xl

data = []  # Lista para almacenar los valores en cada iteración
def f(x):
    return 2 * np.sin(x) - x**2 / 10

def dorada(xl, xu):
    error = abs(xu - xl)
    d = 0.618*(xu - xl)
    x1 = xl + d 
    x2 = xu - d
    fx1 = f(x1)
    fx2 = f(x2)

            
        
    if error <= tolerancia:
            df = pd.DataFrame(data, columns=["xu", "xl", "x1", "x2", "error"])
            return df
    else:
            if fx2 > fx1:
                xu = x2
                data.append([xu, xl, x1, x2, error])
                return dorada(xl, xu)  
            elif fx2 < fx1:
                xl = x1
                data.append([xu, xl, x1, x2, error])
                return dorada(xl, xu)  
            else:
                
                return x1
    


root = dorada(xl, xu)
print(root)
