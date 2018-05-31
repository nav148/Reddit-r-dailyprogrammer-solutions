#-------------------------------------------------------------------------------
# Name:        [2017-12-11] Challenge #344 [Easy] Baum-Sweet Sequence
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7j33iv/20171211_challenge_344_easy_baumsweet_sequence/
# Created:     08/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def baum_term(n):
    bin_n = bin(n)[2:]
    if n == 0:
        return 1
    count = 0
    for (i, val) in enumerate(bin_n):
        if val == '0':
            count += 1
            if i == len(bin_n)-1 and count % 2 == 1:
                return 0
        else:
            if count % 2 == 1:
                return 0
            count = 0
    return 1

def baum_seq(n):
    baum_sequence = []
    for i in range(n+1):
        baum_sequence.append(baum_term(i))
    print(baum_sequence)

baum_seq(20)