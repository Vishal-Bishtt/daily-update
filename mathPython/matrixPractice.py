import numpy as np
a= np.array([
    [4,3,2],
    [1,4,1],
    [3,10,4]
])
eginvalue , eginvactor = np.linalg.eig(a)
largeeginvalue = np.max(eginvalue)
print("Eginvalue: ", eginvalue)
print("Largest Eginvalue: ", largeeginvalue)