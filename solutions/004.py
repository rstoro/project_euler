#!/usr/bin/env python3


#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


def find_palindrome(n_digits):
    is_palendrome = lambda s: s[:len(s)] == s[len(s)-1::-1] if len(s) % 2 == 0 else False
    max_ab = int('9' * n_digits)

    #NOTE: can this be faster?  is there a way to find the largest palindrome 
    #without finding all of the palindromes?  as it stands, this seems naive.
    palendromes = []
    for a in range(max_ab, 1, -1):
        for b in range(max_ab, 1, -1):
            product = b * a 
            if is_palendrome(str(product)):
                palendromes.append(product)

    return max(palendromes)


if __name__ == '__main__':
    solution = find_palindrome(3)
    print(solution)


