base = {}

with open("backend/mcc_desc.txt") as file:
    for line in file:
        code, description = line.strip().split(' ', 1)
        if description not in base:
            base[description] = []
        base[description].append(code)

print(base["Restaurants"])