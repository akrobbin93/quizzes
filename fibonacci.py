#----------------------------------------
#fibonacci.py
#Author: akrobbin93
#Quiz: Input number as position, find its fibonacci
#sequence value
#----------------------------------------

#----------------------------------------
#Fibonacci Sequence:
# 0 1 1 2 3 5 8 13 21 34
#----------------------------------------

def getNthfibonacci(n):
    if n == 1:
        return 0
    if n <= 3:
        return 1
    return getNthfibonacci(n-1) + getNthfibonacci(n-2)
#----------------------------------------
def getNthFib(n, calculated = {1:0, 2:1, 3:1}):
    if n in calculated:
        return calculated[n]
    calculated[n] = getNthFib(n-1, calculated) + getNthFib(n-2, calculated)
    return calculated[n]
#----------------------------------------

print(getNthfibonacci(20))
print(getNthFib(100))
