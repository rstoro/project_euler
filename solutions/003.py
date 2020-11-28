#!/usr/bin/env python3


#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?


def get_largest_prime_factors(n):
    s_p = 1
    while True:
        s_p += 1
        if n % s_p == 0:
            factor = n // s_p 
            if not any( factor % i == 0 for i in range(2, factor) ):
                return factor


if __name__ == '__main__':
    solution = get_largest_prime_factors(600851475143)
    print(solution)
