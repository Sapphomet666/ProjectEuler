max = [0, 0]
for i in range(1, 1000000):
    steps = 0
    j = i
    while j != 1:
        if j % 2 == 0:
            steps = steps + 1
            j = j // 2
        else:
            steps = steps + 1
            j = 3 * j + 1
    if steps > max[1]:
        max = [i, steps]
print(max)


