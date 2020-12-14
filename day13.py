with open("input_day13.txt") as f:
    notes = f.read().splitlines()

# Part one
timestamp = int(notes[0])
buses = [int(b) for b in notes[1].split(",") if b != "x"]

ts = timestamp
depart = []
while True:
    for bus in buses:
        if ts % bus == 0:
            depart = [ts, bus]
            break
    if depart:
        break
    ts += 1

print((depart[0] - timestamp) * depart[1])

# Part Two
def gcd(a,b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = gcd(b % a, a)
    return (g, x - (b // a) * y ,y)

def modular_inverse(n, p):
    g, inv, y = gcd(n, p)
    assert g == 1
    return inv % p

def chinese_remainder_theorem(buses, modulo):
    x = 0
    for a, p in buses.items():
        n = modulo // p
        inverse = modular_inverse(n, p)
        x = (x+a*n*inverse) % modulo
    return x % modulo

buses = {-i: int(b) for i, b in enumerate(notes[1].split(",")) if b != "x"}
modulo = 1
for i in buses:
    modulo *= buses[i]
print(chinese_remainder_theorem(buses, modulo))