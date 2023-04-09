for i in range(0,333):
    for j in range(333,500):
        if pow(i,2)+pow(1000-j-i,2) == pow(j,2):
            list = [i,1000-i-j,j]
            print(list)
            print(i*j*(1000-i-j))