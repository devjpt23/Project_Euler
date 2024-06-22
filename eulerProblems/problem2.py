def fib(a):
    if (a == 0) or (a == 1):
        return 1
    else:
        return fib(a-1) + fib(a-2)
    
x=0
sum=0

while fib(x) < 4000000:
    if fib(x) % 2 == 0:
        sum += fib(x)
        x += 1  
    else:
        x+=1

print(sum)
print(fib(10))