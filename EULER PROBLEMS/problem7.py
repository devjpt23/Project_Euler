# flag = False
# n = 13

# for i in range(2,n):
#     if(n % i == 0 ):
#         flag = True
#         break

# if flag:
#     print("is not a prime number")
# else:
#     print("prime number")



numbers = [2,3,4,5,6,7,8]
flag = False
prime_counter = 0
prime = []


for i in range(2,125000):
    for x in range(2,i):
        if (i % x == 0):
            
            # print(f"{i} is not prime prime ")
            
            break
    else:
        print(f"{i} is prime number ")
        prime_counter += 1
        prime.append(i)

print(prime)
print(f" {prime[-1]} is the last prime number in this seq")
print(f"there are {prime_counter} prime numbers")
print(f"fourth number is {prime[10000]}")

    









