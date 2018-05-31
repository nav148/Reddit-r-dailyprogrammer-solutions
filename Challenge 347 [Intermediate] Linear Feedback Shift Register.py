#-------------------------------------------------------------------------------
# Name:        [2018-01-17] Challenge #347 [Intermediate] Linear Feedback Shift Register
# Purpose:
#
# Author:      navin
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7r17qr/20180117_challenge_347_intermediate_linear/
# Created:     15/02/2018
# Copyright:   (c) navin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re

def LFSR(strng):
    split = list(strng.split())
    taps = list(map(int, re.findall('\d+', split[0])))
    gate = split[1]
    init_val = split[2]
    output_steps = int(split[3])

    print('0', init_val)
    previous = init_val
    for i in range(1, output_steps+1):
        total = 0
        for val in taps:
            total += int(previous[val])
        if gate == 'XOR':
            if total == 1:
                next_step = '1'
            else:
                next_step = '0'
        else:
            if total == 1:
                next_step = '0'
            else:
                next_step = '1'

        next_step += previous[:-1]
        print(i, next_step)
        previous = next_step



#LFSR('[0,2] XOR 001 7')
#LFSR('[1,2] XOR 001 7')
#LFSR('[0,2] XNOR 001 7')
LFSR('[1,2,3,7] XOR 00000001 16')
LFSR('[1,5,6,31] XOR 00000000000000000000000000000001 16')
