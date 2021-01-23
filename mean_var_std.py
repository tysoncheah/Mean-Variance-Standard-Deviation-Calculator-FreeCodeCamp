import numpy as np

def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    
    x = np.array(list).reshape(3,3)
    cal = {k:[func(x, axis=ax).tolist() 
    for ax in (0,1,None)]
    
    for (k,func) in zip(["mean", "variance", "standard deviation", "max", "min", "sum"], 
             [np.mean, np.var, np.std, np.max, np.min, np.sum])
    }

    return cal