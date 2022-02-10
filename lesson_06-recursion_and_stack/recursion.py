# non-recursive
def facto(n):
    """calculating n factorial"""
    i=1
    while n>1:
        i = i*n
        n-=1
    return i

print(facto(5))


# recursive
def factorial(N):
    """N factorial with recursion"""
    if N>1:
        return N*factorial(N-1)
    else:
        return 1

print(factorial(5))
