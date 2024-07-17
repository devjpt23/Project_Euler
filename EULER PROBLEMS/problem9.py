# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))

# if (a < b < c):
#     sqaureA = a ** 2
#     sqaureB = b ** 2 
#     sqaureC = c ** 2

#     print(f"{sqaureA} + {sqaureB} = {sqaureC}")
# else:
#     pass


def A_number(number):
    for a in range(number):
        return a
    
def B_number(number):
    for b in range(number):
        return b
def C_number(number):
    for c in range(number):
        return c

print(A_number(100))