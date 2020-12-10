import itertools

numbers = []
with open("input_day10.txt") as f:
    for line in f.read().splitlines():
        numbers.append(int(line))

numbers.append(max(numbers)+3)
numbers.sort()
oneJolt = 0
threeJolt = 0
rating = 0
for n in range(len(numbers)):
    diff = numbers[n] - rating
    if(diff == 1): oneJolt += 1
    if(diff == 3): threeJolt += 1
    rating = numbers[n]

print(oneJolt * threeJolt)


# part 2
sol = {0:1}
for line in numbers:
    sol[line] = 0
    if line - 1 in sol:
        sol[line]+=sol[line-1]
    if line - 2 in sol:
        sol[line]+=sol[line-2]
    if line - 3 in sol:
        sol[line]+=sol[line-3]

print(sol[max(numbers)])

