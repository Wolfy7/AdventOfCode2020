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
ship = [0, 0]
facing = 1
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action in ["L", "R"]:
        steps = value / 90
        if action == "L":
            facing = int((facing - steps) % len(directions))
        else:
            facing = int((facing + steps) % len(directions))
    elif action == "F":
        ship = movePos(directions[facing], value, ship)
    else:
        ship = movePos(action, value, ship)

print(abs(ship[0]) + abs(ship[1]))

ship = [0, 0]
waypoint = [1, 10, 0, 0]
for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action in ["L", "R"]:
        steps = value // 90
        if action == "L":
            for i in range(steps):
                waypoint = waypoint[1:] + [waypoint[0]]
        else:
            for i in range(steps):
                waypoint = [waypoint[3]] + waypoint[:3]
    elif action == "F":
        ship[0] += value * (waypoint[0] - waypoint[2])
        ship[1] += value * (waypoint[1] - waypoint[3])
    else:
        if action == "N":
            waypoint[0] += value
        elif action == "S":
            waypoint[2] += value
        elif action == "E":
            waypoint[1] += value
        elif action == "W":
            waypoint[3] += value

print(abs(ship[0]) + abs(ship[1]))