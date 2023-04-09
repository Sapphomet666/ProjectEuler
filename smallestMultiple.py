def GCD(a,b):
    while a !=0:
        if a>b:
            c=a
            a=b
            b=c
        b=b-a
    return b

num=1
for i in range (1,21):
    num=num*i/GCD(num,i)
print(num)
