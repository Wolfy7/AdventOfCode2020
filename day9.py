with open("input_day9.txt") as f:
    numbers = f.read().splitlines()

# Part one
index = 25
preamble = [int(i) for i in numbers[:index]]
while True:
    check = int(numbers[index])
    valid = False
    for n in preamble[index-25:]:
        if (check - n != n) and (check - n in preamble):
            valid = True
            break
        else:
            valid = False
    if not valid:
        break
    #del preamble[0]
    preamble.append(check)
    index += 1

print(check)

# Part two
contiguous = []
index = 0
while True:
    found = False
    for i in preamble[index:]:
        contiguous.append(i)
        if len(contiguous) < 2: continue
        if sum(contiguous) == check:
            found = True
            break
        elif sum(contiguous) > check:
            index += 1
            contiguous = []
            break
    if found:
        break

print(min(contiguous) + max(contiguous))