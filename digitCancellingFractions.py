def isCurious(fraction):
    if fraction[1] * (fraction[0] % 10) == fraction[0] * (fraction[1] // 10) and (fraction[1] % 10) == (fraction[0] // 10):
        return True
    if fraction[0] * (fraction[1] % 10) == fraction[1] * (fraction[0] // 10) and (fraction[0] % 10) == (fraction[1] // 10):
        return True
    return False

def GCD(intA, intB):
    while intB != 0:
        if intB > intA:
            c = intA
            intA = intB
            intB = c
        intA += -1 * intB

    return intA


def curiosCleaner(curiousFracs):
    for i in range(0, len(curiousFracs)):
        if curiousFracs[i][0] == curiousFracs[i][1]:
            curiousFracs[i] = -1
    list = []
    for i in range(0, len(curiousFracs)):
        if curiousFracs[i] != -1:
            list.append(curiousFracs[i])
    return(list)


curiousFracs = []
for i in range(10, 100):
    for j in range(i, 100):
        if isCurious([i, j]):
            curiousFracs.append([i,j])

curiousFracs = curiosCleaner(curiousFracs)
print(curiousFracs)

frac = [1, 1]
for x in curiousFracs:
    frac = [frac[0] * x[0], frac[1] * x[1]]

divisor = GCD(frac[0], frac[1])
frac = [frac[0] // divisor, frac[1] // divisor]
print(frac)

