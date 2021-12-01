import pathlib
from numpy import loadtxt

current_dir: str = str(pathlib.Path.cwd())
input = loadtxt(current_dir + "/input.txt", dtype =int)

count: int = 0

for idx, val in enumerate(input):
    if (idx + 3 == len(input)):
        print(count)
        break
    else:
        current_window = input[idx] + input[idx + 1] + input[idx + 2]
        next_window = input[idx + 1] + input[idx + 2] + input[idx + 3]
        if current_window < next_window:
            # print(str(current_window) + " - " + str(next_window))
            count = count + 1