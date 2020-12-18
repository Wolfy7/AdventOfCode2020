import re

with open("input_day18.txt") as f:
    lines = f.read().splitlines()


def resolve(equation):
    regular_match = re.compile(r"(\d+) ([+*]) (\d+)")
    replace_parentheses = re.compile(r"\((\d+)\)")

    while True:
        equation = re.sub(replace_parentheses, r"\1", equation)

        if match := re.search(regular_match, equation):
            x, operator, y = match.groups()
            if operator == "+":
                val = int(x) + int(y)
            elif operator == "*":
                val = int(x) * int(y)
            equation = equation[:match.start()] + str(val) + equation[match.end():]
        else:
            return int(equation)


def resolve2(line):
    tokens = line.split(" ")
    idcs = [i for i, t in enumerate(tokens) if t == "+"]
    for i in idcs:
        tokens[i-1] = '(' + tokens[i-1]
        tokens[i+1] = tokens[i+1] + ")"
    string = ' '.join(tokens)
    return eval(string)

part_1 = 0
part_2 = 0
for line in lines:
    part_1 += resolve(line[:])
    part_2 += resolve2(line[:])

print(part_1)
print(part_2)
