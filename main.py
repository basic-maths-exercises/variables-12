import numpy as np 

fibonacci = np.zeros(100)
fibonacci[0], fibonacci[1]=1,1
for i in range(2,100) : 
  fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

print( fibonacci )

