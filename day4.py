import re
passpords = []
passpord = {}
with open("input_day4.txt") as f:
    for line in f:
        line = line.strip()
        if(len(line) > 0):
            for pd in line.split(" "):
                key, value = pd.partition(":")[::2]
                passpord[key] = value
        else:
            passpords.append(passpord)
            passpord = {}
passpords.append(passpord)

# Part one
valid = 0
fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for p in passpords:
    #if( all( v in p for v in fields)):
    if fields.issubset(p.keys()):
        valid += 1

print(valid)

# Part two
valid = 0
for p in passpords:
    if fields.issubset(p.keys()):
        p_valid = True
        for key in fields:
            if(key == "byr"):
                byr = int(re.search("[0-9]{4}", p["byr"]).group())
                if not (1920 <= byr <= 2002):
                    p_valid = False
                    break
            if(key == "iyr"):
                iyr = int(re.search("[0-9]{4}", p["iyr"]).group())
                if not (2010 <= iyr <= 2020):
                    p_valid = False
                    break
            if(key == "eyr"):
                eyr = int(re.search("[0-9]{4}", p["eyr"]).group())
                if not (2020 <= eyr <= 2030):
                    p_valid = False
                    break
            if(key == "hgt"):
                x = re.search("([0-9]+)(cm|in)", p["hgt"])
                if(x):
                    v = int(x.group(1))
                    u = x.group(2)
                    if(u == "cm"):
                        if not (v >= 150 and v <= 193):
                            p_valid = False
                            break
                    if(u == "in"):
                        if not (v >= 59 and v <= 76):
                            p_valid = False
                            break
                else:
                    p_valid = False
                    break
            if(key == "hcl"):
                x = re.search("#[0-9a-f]{6}", p["hcl"])
                if not(x):
                    p_valid = False
                    break
            if(key == "ecl"):
                x = re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", p["ecl"])
                if not(x):
                    p_valid = False
                    break
            if(key == "pid"):
                x = re.search("^[0-9]{9}$", p["pid"])
                if not(x):
                    p_valid = False
                    break
        if(p_valid):
            valid += 1

print(valid)


