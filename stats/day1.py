# Enter your code here. Read input from STDIN. Print output to STDOUT
values = int(input())

numbers = list(map(int, input().split()))
n = len(numbers)
mean = sum(numbers) / n

print(round((sum([(x - mean)**2 for x in numbers]) /n )**0.5, 1))

# Enter your code here. Read input from STDIN. Print output to STDOUT

import statistics as st

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if n%2 != 0:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2+1:])
else:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])

ir = round(float(q3-q1), 1)
print(ir)