import pathlib
from typing import Match

current_dir: str = str(pathlib.Path.cwd())

depth: int = 0
horizontal: int = 0
aim: int = 0 

with open(current_dir + "/input.txt") as file:
    for line in file:
        instruction: str = line.split()[0] 
        value: int = int(line.split()[1])
        
        if(instruction == 'forward'):
            horizontal += value
            depth += (aim * value)
        elif(instruction == 'down'):
            aim += value
        elif(instruction == 'up'):
            aim -= value

print(depth * horizontal)