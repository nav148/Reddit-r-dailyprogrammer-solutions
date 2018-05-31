#-------------------------------------------------------------------------------
# Name:        [2018-01-24] Challenge #348 [Intermediate] Bowling Frames Display
# Purpose:
#
# Author:      navin
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7so37o/20180124_challenge_348_intermediate_bowling/
# Created:     14/02/2018
# Copyright:   (c) navin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def bowling_scores(strng):
    pins_knocked = list(map(int, strng.split()))
    frames = [0]*10
    pin_index = 0
    for i in range(len(frames)):
        if i < 9 or (i == 9 and len(pins_knocked[pin_index:]) == 2):
            if pins_knocked[pin_index] != 10:
                if pins_knocked[pin_index] + pins_knocked[pin_index+1] == 10:
                    frames[i] = str(pins_knocked[pin_index]) + '/'
                elif pins_knocked[pin_index+1] == 0:
                    frames[i] = str(pins_knocked[pin_index]) + '-'
                else:
                    frames[i] = str(pins_knocked[pin_index]) + str(pins_knocked[pin_index+1])
                pin_index += 2
            else:
                frames[i] = 'X'
                pin_index += 1
        else:
            if pins_knocked[pin_index] == 10:
                frames[i] = 'XXX'
            else:
                frames[i] = str(pins_knocked[pin_index]) + '/' + str(pins_knocked[pin_index+2])
    print(("{:<3}"*10).format(*frames))

bowling_scores("6 4 5 3 10 10 8 1 8 0 10 6 3 7 3 5 3")
bowling_scores("9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0")
bowling_scores("10 10 10 10 10 10 10 10 10 10 10 10")
bowling_scores("5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5")
bowling_scores("10 3  7  6  1  10 10 10 2  8  9  0  7  3  10 10 10")
bowling_scores("9  0  3  7  6  1  3  7  8  1  5  5  0  10 8  0  7  3  8  2  8")