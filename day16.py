import re

state = 0
match_fields = []
nearby_tickets = []
with open("input_day16.txt") as f:
    for line in f.read().splitlines():
        if line == "": continue
        if state == 0:
            match = re.match("([a-z ]+): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)", line)
            if match != None:
                match_fields.append(match)
            else:
                state = 1
        elif  state == 1:
            if line == "your ticket:": continue
            your_ticket = line.strip().split(",")
            state = 2
        elif  state == 2:
            if line == "nearby tickets:": continue
            nearby_tickets.append(line.strip().split(","))

valid_numbers = set()
fields = {}
for field in match_fields:
    fields[field.group(1)] = set()
    for x in range(int(field.group(2).split("-")[0]), int(field.group(2).split("-")[1])+1):
        valid_numbers.add(x)
        fields[field.group(1)].add(x)
    for x in range(int(field.group(3).split("-")[0]), int(field.group(3).split("-")[1])+1):
        valid_numbers.add(x)
        fields[field.group(1)].add(x)

invalid_numbers = []
valid_nearby_tickets = nearby_tickets[:]
for ticket in nearby_tickets:
    for number in ticket:
        if int(number) not in valid_numbers:
            invalid_numbers.append(int(number))
            valid_nearby_tickets.remove(ticket)
# Part one
print(sum(invalid_numbers))

# Part two
possibilities = {i: list(fields.keys()) for i in range(len(nearby_tickets[0]))}

for t in valid_nearby_tickets:
    for counter, v in enumerate(t):
        for key in fields.keys():
            possible = False
            if int(v) in fields[key]:
                possible = True
            if not possible and key in possibilities[counter]:
                possibilities[counter].remove(key)

changed = True
while changed:
    changed = False
    for key in possibilities:
        if len(possibilities[key]) == 1:
            to_delete = possibilities[key][0]
            for i in possibilities:
                if i == key or not to_delete in possibilities[i]:
                    continue
                possibilities[i].remove(to_delete)
                changed = True
part2 = 1
for i in possibilities:
    if "departure " in possibilities[i][0]:
        part2 *= int(your_ticket[i])
print(part2)