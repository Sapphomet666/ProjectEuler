def factorial(number):
    prod = 1
    for i in range(1, number + 1):
        prod = prod * i
    return prod

def choose(big, small):
    X = factorial(big) // (factorial(small) * factorial(big - small))
    return X

print(choose(40, 20))
