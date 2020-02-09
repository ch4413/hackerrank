import numpy as np
from scipy import stats
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())

b =  list(map(int, input().split()))

c = np.array(b)
print(np.mean(c))
print(np.median(c))
print(stats.mode(c).mode[0])
