#!/usr/bin/env python3
from functools import reduce


#The sum of the squares of the first ten natural numbers is, 
#1^2 + 2^2 + ... + 10^2 = 385
#
#The square of the sum of the first ten natural numbers is, 
#(1+2+ ... +10)^2 == 55^2 = 3025
#
#Hence the difference between the sum of the squares of the first 
#ten natural numbers and the square of the sum is
#3025 - 385 = 2640
#
#
#Find the difference between the sum of the squares of the first 
#one hundred natural numbers and the square of the sum.


def sum_square_dif(s):
    #sum(s) * sum(s) may be faster
    #'*' is strongly rooted in processing, while '**' is a wrapper for Math.pow
    square_of_sum = sum(s) ** 2
    sum_of_squares = reduce(lambda a, b: a + b * b, s, 0)
    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    solution = sum_square_dif( [i+1 for i in range(0, 100)] )
    print(solution)

