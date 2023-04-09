fibbi=[0,1]

while fibbi[-1]<100:
    fibbi=fibbi+[fibbi[-1]+fibbi[-2]]
fibbi=fibbi[:-1]

partialSum=0
for entry in fibbi:
    if entry%2==0:
        partialSum=partialSum+entry

print(partialSum)



