phi = 1.618033988749
root5 = 2.2360679775
digits = 1
fibo = 1 / root5
index = 0
while digits < 1000:
    fibo = fibo * phi
    index += 1
    if fibo > 10:
        fibo = fibo / 10
        digits += 1
print(index)