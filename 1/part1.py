import pathlib

current_dir: str = str(pathlib.Path.cwd())

count: int = 0
prev: int = -1 

with open(current_dir + "/input.txt") as file:
    for line in file:
        if (prev < int(line) and prev != -1):
            print(str(prev) + " - " + line)
            count += 1
        prev = int(line)

print(count)
