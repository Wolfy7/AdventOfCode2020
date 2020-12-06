lines = []
with open("input_day6.txt") as f:
    lines = f.read().split("\n\n")

sum = 0
sum2 = 0
for l in lines:
    answers = set(l.replace("\n", ''))
    sum += len(answers)
    # Part two
    groups = l.split("\n")
    a = set(groups[0])
    for l in range(1, len(groups)):
        a.intersection_update(groups[l])
    sum2 += len(a)
print(sum)
print(sum2)