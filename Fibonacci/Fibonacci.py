import time
import numpy as np
import matplotlib.pyplot as plt

def DPFib(n):

    F = list((0,1))
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[n]

def RecursiveFib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (RecursiveFib(n-1) + RecursiveFib(n-2))

# Fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


dp_history = list()
recursive_history = list()

for index in range(0, 40):
    print("INDEX VALUE: ", index)
    startTime = time.clock()
    DPFib(index)
    endTime = time.clock()
    dp_time = endTime - startTime
    print("Dynamic Programming Time: ", dp_time)
    dp_history.append(dp_time)

    startTime = time.clock()
    RecursiveFib(index)
    endTime = time.clock()
    recursive_time = endTime - startTime
    print("Recursive Time: ", recursive_time)
    recursive_history.append(recursive_time)

plt.plot(dp_history, label='DP')
plt.plot(recursive_history, label='Rec')
plt.ylabel('O(Time) [sec]', size=20)
plt.xlabel('Index Value', size=20)
plt.title('Dynamic Programming vs Recursive Function\nFibonacci Sequence', size=15)
plt.legend()
plt.show()