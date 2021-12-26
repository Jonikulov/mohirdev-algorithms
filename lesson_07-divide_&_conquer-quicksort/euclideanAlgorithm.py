# Euclidean algorithm - greatest common divisor (gcd)

def euclideanAlgorithm(a,b):
    if a<b:
        a,b=b,a

    while True:
        num=a%b
        if num==0:
            break
        a,b=b,num

    return b

print(euclideanAlgorithm(1500,500)) # -> 500
print(euclideanAlgorithm(45,27)) # -> 9

print(euclideanAlgorithm(500,1500)) # -> 500
print(euclideanAlgorithm(27,45)) # -> 9

# answer: with recursion
def gcd(a, b):
    if a == 0 :
        return b      
    return gcd(b%a, a)