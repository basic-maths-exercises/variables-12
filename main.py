import numpy as np 

fibonacci = np.ones(100)
for i in range(2,100) :
  fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

print( fibonacci )
