def fibo(n):
    if(n==0) or (n==1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("enter the amount of numbers you'd like:- "))

for i in range(1,n+1):
    print(f"{fibo(i)}, ",end="")
