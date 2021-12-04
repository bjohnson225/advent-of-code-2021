import pathlib
from numpy import loadtxt 
import numpy as np

current_dir: str = str(pathlib.Path.cwd())

with open(current_dir + "/input.txt") as data:
    input = data.read().split('\n\n')
    selected_nums = list(map(int, input[0].split(',')))

    bingo_cards = []

    for x in range(1, len(input)): 
        card = input[x].splitlines()
        # card = [list(map(int, i.split())) for i in card]
        card = [ i.split() for i in card]

        bingo_cards.append(card)

def vertical_bingo(card):
    l = list()
    
    for i, e in enumerate(card):
        s = set()
        for entry in card:
            s.add(entry[i])
        l.append(s)
    
    for entry in l:
        if(len(entry) == 1):
            return True
    
    return False

def horizontal_bingo(card):
    l = list()
    for i, entry in enumerate(card):
        l.append(set(card[i]))

    for entry in l:
        if(len(entry) == 1):
            return True
    
    return False

def play():
    for num in selected_nums: 
        for i, card in enumerate(bingo_cards):
            # print(card)
            for j, row in enumerate(card):
                try:
                    # print(num)
                    idx = row.index(str(num))
                    row[idx] = 'X'
                    if(horizontal_bingo(card) or vertical_bingo(card)):
                        # print(num)
                        # print(bingo_cards[i])
                        return num, bingo_cards[i]
                except ValueError:
                    continue

answer1, answer2 = play()
answer2 = [item for sublist in answer2 for item in sublist]
answer2 = list(map(int,filter(lambda x: x != 'X', answer2)))

print(answer1 * sum(answer2))
