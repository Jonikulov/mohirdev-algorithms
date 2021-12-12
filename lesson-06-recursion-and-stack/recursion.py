# calculating n factorial
def facto(n):
    i=1
    while n>0:
        i = i*n
        n-=1
    return i

print(facto(5))

# N factorial with recursion
def factorial(N):
    if N>0:
        return N*factorial(N-1)
    else:
        return 1

print(factorial(5))