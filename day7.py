
rules = {}
with open("Day7\input_day7.txt") as f:
    for rule in f:
        r = rule.replace("bags", "bag").replace(".", "").strip().split(" contain")
        rules[r[0]] = r[1].split(", ")

# Part one
def canContainShiny(rule):
    ret = False
    for r in rules[rule]:
        r = "".join([i for i in r if (not i.isdigit())]).lstrip()
        if("shiny gold" in r):
            ret = True
            break
        if("no other bag" in r):
            ret = False
        else:
            ret = canContainShiny(r)
        if(ret): break
    return ret

bagColors = 0
for rule in rules:
    if(canContainShiny(rule)):
        bagColors += 1
print(bagColors)

#Part two
def countBags(bag):
    ret = 0
    for r in rules[bag]:
        if("no other bag" in r):
            ret = 0
            break
        num = int(r.strip().split(" ")[0])
        bag = "".join([i for i in r if (not i.isdigit())]).lstrip()
        ret += num + (num * countBags(bag))
    return ret

print(countBags("shiny gold bag"))