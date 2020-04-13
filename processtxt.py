import numpy as np
a = np.zeros([1,3], dtype=int)
for line in open('detection.txt'):
  if len(line.split()) > 0:
    i = 0
    while 3*i < len(line.split()):
      b = np.array([[int(line.split()[3*i]), int(line.split()[3*i+1]), int(line.split()[3*i+2])]])
      a = np.concatenate((a,b), axis=0)
      i+=1
a = a.astype('int16')
a = a[a[:,0].argsort(kind='mergesort')]
a = np.delete(a,0,0)
