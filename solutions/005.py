#!/usr/bin/env python3
from functools import reduce


#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all 
#of the numbers from 1 to 20?
#


def get_smallest_multiple(s):
    #NOTE: What do we know?
    #It has to be an even number
    #It has to be a multiple of the largest number in the set
    #It has to be less than the product of the set (can this be reduced?)
    for i in range(2, reduce(lambda a, b: a * b, s), 2):
        if all(i % n == 0 for n in s):
            return i



if __name__ == '__main__':
    solution = get_smallest_multiple( [i+1 for i in range(0, 20)] )
    print(solution)

