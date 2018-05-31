#-------------------------------------------------------------------------------
# Name:        [2017-12-04] Challenge #343 [Easy] Major scales
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7hhyin/20171204_challenge_343_easy_major_scales/?sort=top
# Created:     09/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from collections import deque

def note(scale_name, solfege_name):
    solfege = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9, 'Ti':11 }
    scale_dict = {'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4, 'F':5, 'F#':6, 'G':7, 'G#':8, 'A':9, 'A#':10, 'B':11}
    scale = deque(['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])

    scale.rotate(-scale_dict[scale_name])
    print(scale[solfege[solfege_name]])

note("C", "Do")
note("C", "Re")
note("C", "Mi")
note("D", "Mi")
note("A#", "Fa")




