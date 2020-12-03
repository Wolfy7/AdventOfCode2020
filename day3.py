lines = []
with open("input_day3.txt") as f:
    lines = f.readlines()

def getTress(right, down):
    trees = 0
    pos = 0
    pattern_len = 31
    for i, line in enumerate(lines):
        if i == 0: continue
        if(i % down != 0): continue

        pos += right
        if (line[pos % pattern_len] == '#'):
            trees += 1
    return trees

# Part one
Right3Down1 = getTress(3, 1)
print(Right3Down1)

# Part two
Right1Down1 = getTress(1, 1)
Right3Down1 = getTress(3, 1)
Right5Down1 = getTress(5, 1)
Right7Down1 = getTress(7, 1)
Right1Down2 = getTress(1, 2)
print(Right1Down1 * Right3Down1 * Right5Down1 * Right7Down1 * Right1Down2)