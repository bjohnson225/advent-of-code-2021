import pathlib
from typing import Counter, Match
from numpy import loadtxt

current_dir: str = str(pathlib.Path.cwd())
input = loadtxt(current_dir + "/input.txt", dtype = str)

most_common = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

scrubber = input
generator = input
gamma: str = ""
epsilon: str = ""

for i in range(0, 12):
    for line in scrubber:
        digit = line[i]
        if (digit == '1'):
            most_common[i] = most_common[i] + 1
        elif (digit == '0'):    
            most_common[i] = most_common[i] - 1    

    if(most_common[i] >= 0):
        gamma += '1'
    else:
        gamma += '0'
    
    if(len(scrubber) > 1):
        scrubber = list(filter(lambda x: True if (x.startswith(gamma)) else False, scrubber))

most_common = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 12):
    for line in generator:
        digit = line[i]
        if (digit == '1'):
            most_common[i] = most_common[i] + 1
        elif (digit == '0'):    
            most_common[i] = most_common[i] - 1    

    if(most_common[i] >= 0):
        epsilon += '0'    
    else:
        epsilon += '1'           
    
    if(len(generator) > 1):
        generator = list(filter(lambda x: x.startswith(epsilon), generator))


print(scrubber) 
print(generator)

print(int(scrubber[0], 2) * int(generator[0],2) )