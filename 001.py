#!/usr/bin/env python3

#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.


#can we do better than O(n)?
def get_natural_numbers( n, multiples=(3, 5) ):
    for i in range(1, n):
        for mult in multiples:
            if i % mult == 0:
                yield i
                break


if __name__ == '__main__':
    problem = sum(get_natural_numbers(1000))
    print(problem)

