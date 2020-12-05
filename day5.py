lines = []
with open("input_day5.txt") as f:
    lines = f.readlines()

#lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

seats = []
for boardinpass in lines:
    boardinpass = boardinpass.strip()
    row = int( boardinpass[:7].replace("F","0").replace("B","1") ,2)
    col = int( boardinpass[7:].replace("L","0").replace("R","1") ,2)
    boardid = row * 8 + col
    seats.append(boardid)

seats = sorted(seats)
x = set(range(seats[0], seats[-1])) - set(seats)

print("our seat: ", list(x)[0])
print("maximum seat id:", max(seats))