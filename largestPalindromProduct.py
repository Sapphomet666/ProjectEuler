def isPalindrome(pal):

   palStr=str(pal)
   list=range(0,len(palStr))
   n=len(palStr)-1
   palindrome=True
   for digit in list:
       if palStr[digit] != palStr[n-digit]:
           palindrome=False
   return(palindrome)

#print(isPalindrome(1))

palList=[]
for i in range(100,999):
    for j in range(i,999):
        if isPalindrome(i*j):
            palList.append(i*j)

print(max(palList))