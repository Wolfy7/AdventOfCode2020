
import re
with open("input_day14.txt") as f:
    program = f.read().splitlines()

# Part one
mem = {}
mask = ""
for action in program:
    a, v = action.split(" = ")
    if a == "mask":
        mask = v
    else:
        address = re.match("mem\[([0-9]+)\]", a).group(1)
        t = "0b"
        x = bin(int(v))[2:]
        for i, c in enumerate(mask):
            i = 35 - i
            if c == 'X':
                l = len(x) - 1
                if i <= l:
                    t += (x[l- i])
                else:
                    t += "0"
            else:
                t += c
        mem[address] = t

result = 0
for m in mem.values():
    result += (int(m, 2))
print(result)

# Part two
import itertools
mem = {}
for action in program:
    a, v = action.split(" = ")
    if a == "mask":
        mask = v
    else:
        address = re.match("mem\[([0-9]+)\]", a).group(1)
        t = ""
        x = bin(int(address))[2:]
        for i, c in enumerate(mask):
            i = 35 - i
            if c == 'X':
                t += c
            elif c == '0':
                l = len(x) - 1
                if i <= l:
                    t += (x[l- i])
                else:
                    t += "0"
            else:
                t += "1"

        for floating in list(itertools.product(["0", "1"], repeat=t.count("X"))):
            a = t
            for f in floating:
                x = a.find("X")
                a = a[:x] + f + a[x+1:]
            mem[int(a, 2)] = int(v)
print(sum(mem.values()))
