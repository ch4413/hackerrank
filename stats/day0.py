import numpy as np
from scipy import stats
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())

b = list(map(int, input().split()))

c = np.array(b)
print(np.mean(c))
print(np.median(c))
print(stats.mode(c).mode[0])

# Enter your code here. Read input from STDIN. Print output to STDOUT
values = int(input())

numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

sum_tot = sum([numbers[i]*weights[i] for i in range(len(numbers))])
sum_weights = sum(weights)
print(round(sum_tot / sum_weights, 1))