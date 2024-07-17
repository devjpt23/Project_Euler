def ispalidrome(n):
    strinfy = str(n)
    return strinfy == strinfy[::-1]

result = ispalidrome(900009)
palindromeNumbers = []
for i in range(100,1000):
    for j in range(100,1000):
        number = j * i
        result = ispalidrome(number)
        if result == True:
            palindromeNumbers.append(number)
        else:
            continue


print(max(palindromeNumbers))