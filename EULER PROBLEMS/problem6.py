n = 100
sum_of_the_squares = 0
for i in range(1,n+1):
    sum_of_the_squares += i ** 2


square_of_the_sum = 0
for j in range(1,n+1):
    square_of_the_sum += j
    sqaure_of_sum_fin = (square_of_the_sum) ** 2

diff = (sqaure_of_sum_fin) - (sum_of_the_squares) 
print(diff)

