
def getSpokenNumber(n):
    starting_numbers = [6,13,1,15,2,0]
    numbers = {number: [turn] for turn, number in enumerate(starting_numbers, start=1)}
    last_number = starting_numbers[len(starting_numbers)-1]
    for turn in range(len(starting_numbers)+1,n+1):
        spoken = len(numbers[last_number])
        if spoken <= 1:
            numbers[0].append(turn)
            last_number = 0
            continue
        else:
            number = numbers[last_number][-1] - numbers[last_number][-2]
            if number in numbers:
                numbers[number].append(turn)
            else:
                numbers[number] = [turn]
            last_number = number
    return(last_number)

# Part one
print(getSpokenNumber(2020))
# Part two
print(getSpokenNumber(30000000))

