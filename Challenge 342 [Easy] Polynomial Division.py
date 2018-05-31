#-------------------------------------------------------------------------------
# Name:        [2017-11-27] Challenge #342 [Easy] Polynomial Division
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7fvy7z/20171127_challenge_342_easy_polynomial_division/
# Created:     09/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def poly_div(poly_one, poly_two):
    dividend = poly_one[:]
    divisor = poly_two[:]
    solution = []
    while len(dividend) >= len(divisor):
        multi = [x * (dividend[0] // divisor[0]) for x in divisor]
        solution.append((dividend[0] // divisor[0]))
        for (i, val) in enumerate(multi):
            dividend[i] -= val
        del dividend[0]
    print("Solution:",solution)
    print("Remainder:",dividend)

poly_div([4,2,-6,3], [1,-3])
poly_div([2,-9,21,-26,12], [2,-3])
poly_div([10,0,-7,0,-1], [1,-1,3])