def polynomialProduct(polynomialA, polynomialB):
    product = []
    for i in range(0, len(polynomialA)+len(polynomialB) -1):
        product.append(0)
    for i in range(0, len(polynomialA)):
        for j in range(0, len(polynomialB)):
            product[i+j] += polynomialA[i] * polynomialB[j]
    #print((product))
    return product

def coinPolynomial(value, bound):
    polynomial = []
    for i in range(0, bound +1):
        polynomial.append(0)
    for i in range(0, bound +1, value):
        polynomial[i] = 1
    return polynomial

bound = 200
oneP = coinPolynomial(1, bound)
twoP = coinPolynomial(2, bound)
fiveP = coinPolynomial(5, bound)
tenP = coinPolynomial(10, bound)
twentyP = coinPolynomial(20, bound)
fiftyP = coinPolynomial(50, bound)
hundredP = coinPolynomial(100, bound)
twohundredP = coinPolynomial(200, bound)

coins = [oneP, twoP, fiveP, tenP, twentyP, fiftyP, hundredP, twohundredP]
polynominal = [1]
for i in coins:
    polynominal = polynomialProduct(i, polynominal)[:bound +1]
print(polynominal[bound])
