# fibonaci squence
# 1,2,3,5,8... 89
# a sum of all number but, LESS THAN 4000,000

# EULER PROBLEM 2
# recursion

def fibo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


x = 0
sum = 0

while (fibo(x) < 4000000):
    if(fibo(x)%2 == 0):
        sum += fibo(x)
        x += 1
    else:
        x += 1


print(sum)






