import pathlib
from typing import Match
from numpy import loadtxt

current_dir: str = str(pathlib.Path.cwd())
input = loadtxt(current_dir + "/input.txt", dtype = str)

most_common = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in input:
    number = list(line)
    for i, digit in enumerate(number):
        if (digit == '1'):
            most_common[i] = most_common[i] + 1
        elif (digit == '0'):    
            most_common[i] = most_common[i] - 1

print(most_common)

gamma: str = ""
epsilon: str = ""

for entry in most_common:
    if(entry > 0):
        gamma += '1'
        epsilon += '0'    
    else:
        gamma += '0'
        epsilon += '1'   

print(gamma + ' * ' + epsilon)