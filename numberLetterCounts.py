numberSpellings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred",
}

def numToWord(number):
    if number < 20:
        return numberSpellings.get(number)
    if number < 100:
        if number % 10 == 0:
            return numberSpellings.get(number)
        else:
            return numberSpellings.get(number - (number % 10)) + "-" + numberSpellings.get(number % 10)
    if number < 1000:
        if number % 100 == 0:
            return numberSpellings.get(number)
        else:
            return numberSpellings.get(number - (number % 100)) + " and " + numToWord(number % 100)
    if number < 1000000:
        if number % 1000 == 0:
            return numToWord(number // 1000) + " thousand"
        else:
            return numToWord(number // 1000) + " thousand " + numToWord(number % 1000)
    pass

spellingsList = []
total = 0
for i in range(1, 1001):
    spellingsList.append(numToWord(i))
for i in range(0, 1000):
    spellingsList[i] = spellingsList[i].replace("-", " ")
    spellingsList[i] = spellingsList[i].split()
    for j in spellingsList[i]:
        total = total + len(j)
#print(spellingsList)
print(total)

total = 0
print(numToWord(2134))
#for j in spellingsList[200 - 1]:
    #print(j)
    #total = total + len(j)
#print(total)