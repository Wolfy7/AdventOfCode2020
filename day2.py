
with open("input_day2.txt") as f:
    lines = f.readlines()

# Part one
valid = 0
invalid = 0

for line in lines:
    data = line.split(" ")
    policy = data[0]
    least = policy.split('-')[0]
    most = policy.split('-')[1]
    letter = data[1]
    password = data[2]
    letter_appear = password.count(letter.replace(':', ''))
    if(letter_appear >= int(least) and letter_appear <= int(most)):
        valid += 1
    else:
        invalid += 1

print(f"Valid passwords {valid}")
print(f"Invalid passwords {invalid}")

# Part two
valid = 0
invalid = 0

for line in lines:
    data = line.split(" ")
    policy = data[0]
    firstPos = int(policy.split('-')[0]) - 1
    secondPos = int(policy.split('-')[1]) - 1
    letter = data[1].replace(':', '')
    password = data[2].strip()

    if((password[firstPos] == letter) and (password[secondPos] != letter)):
        valid += 1
    elif ((password[firstPos] != letter) and (password[secondPos] == letter)):
        valid += 1
    else:
        invalid += 1

print(f"Valid passwords {valid}")
print(f"Invalid passwords {invalid}")