with open("input_day12.txt") as f:
    instructions = f.read().splitlines()

def movePos(direction, value, position):
    if direction == "N":
        position[0] -= value
    if direction == "S":
        position[0] += value
    if direction == "E":
        position[1] += value
    if direction == "W":
        position[1] -= value
    return position

directions = ["N", "E", "S", "W"]
pos = [0,0]
facing = 1
for instruction in instructions:
    action = instruction[:1]
    value = int(instruction[1:])
    if action in ["L", "R"]:
        steps = value / 90
        if action == "L":
            facing = int((facing - steps) % len(directions))
        else:
            facing = int((facing + steps) % len(directions))
    elif action == "F":
        pos = movePos(directions[facing], value, pos)
    else:
        pos = movePos(action, value, pos)

print(abs(pos[0]) + abs(pos[1]))