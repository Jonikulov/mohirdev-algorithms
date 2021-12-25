# calculating n factorial
def facto(n):
    i=1
    while n>1:
        i = i*n
        n-=1
    return i

print(facto(5))

# N factorial with recursion
def factorial(N):
    if N>1:
        return N*factorial(N-1)
    else:
        return 1

print(factorial(5))