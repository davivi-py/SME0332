import numpy as np

n = 12

seq = np.zeros(n)

seq[0] = 1

seq[1] = 2


def fibonaccia(n):

    seq[n] = seq[n-1] + seq[n-2]

    return seq[n]
for i in range(2,n):


    fibonaccia(i)

print(seq)