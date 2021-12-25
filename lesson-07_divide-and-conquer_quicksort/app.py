def gcd(a, b):
    if a == 0 :
        return b      
    return gcd(b%a, a)

print(gcd(1500,500)) # -> 500
print(gcd(45,27)) # -> 9

print(gcd(500,1500)) # -> 500
print(gcd(27,45)) # -> 9