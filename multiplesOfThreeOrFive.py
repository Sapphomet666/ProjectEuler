#The problem:

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

threeSum=sum(range(0,1000,3))
fiveSum=sum(range(0,1000,5))
fifteenSum=sum(range(0,1000,15))

#Our approach is to use inclusion-exclusion to find the sum.
#By adding up all the multiples of 3 to the multiples of 5, we double count the multiples of 15, so we subtract those out.

threeOrFive=threeSum+fiveSum-fifteenSum
print(threeOrFive)



