# hash functions

def hashfun1(text):
    """accepts text and returns the length of the text"""
    item_len = 0
    for i in text:
        item_len += 1
    return item_len


def hashfun2(text):
    """returns the position of the first letter of the text in the alphabet"""
    order = ord(text[0].lower())
    return order-97


primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
def hashfun3(text):
    """prime numbers & modulo"""
    summ = 0
    for char in text:
        index = ord(char.lower())-97
        summ += primes[index]
    return summ%10


print(hashfun1("12345")) # -> 5
print(hashfun2("apple")) # -> 0
print(hashfun3("bad")) # -> (3+5+2)%10 = 2 