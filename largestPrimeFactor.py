primeTest=600851475143
i=2
while i<pow(primeTest,0.5):
   if primeTest%i==0:
       primeTest=primeTest//i
   else:
       i=i+1
print(primeTest)

