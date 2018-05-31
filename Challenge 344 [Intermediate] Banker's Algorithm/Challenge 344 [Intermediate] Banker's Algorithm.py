#-------------------------------------------------------------------------------
# Name:        [2017-12-13] Challenge #344 [Intermediate] Banker's Algorithm
# Purpose:
#
# Author:      nav
# Link:         https://www.reddit.com/r/dailyprogrammer/comments/
#               7jkfu5/20171213_challenge_344_intermediate_bankers/
# Created:     19/02/2018
# Copyright:   (c) nav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def Bank_algo(t):
    text = open(t, "r")
    lines = text.readlines()
    solution = []
    for (i, val) in enumerate(lines):
        lines[i] = []
        for char in val:
            if char.isdigit():
                lines[i].append(int(char))
    available = lines[0]
    processes = lines[1:]

    for i in range(len(processes)):
        processes[i].append("P"+ str(i))

    maxi = len(processes)
    for i in range(maxi):
        for val in processes:
            if (((available[0] + val[0]) >= val[3]) and ((available[1] + val[1]) >= val[4]) and ((available[2] + val[2]) >= val[5])):
                available[0] += val[0]
                available[1] += val[1]
                available[2] += val[2]
                solution.append(val[-1])
                processes.remove(val)
                break

    if len(solution) == maxi:
        print(*solution)
    else:
        print("No solution found")

Bank_algo("challenge1.txt")