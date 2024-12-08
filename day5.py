with open("inputs/day5.txt", 'r') as inputFile:
    rules, updates = inputFile.read().split("\n\n")
    rules = [list((map(int, line.split("|")))) for line in rules.split("\n")]
    updates = [list((map(int, line.split(",")))) for line in updates.split("\n")]

rule_dict = {}
for a, b in rules:
    if rule_dict.get(a) is None:
        rule_dict[a] = [b]
    else:
        rule_dict[a].append(b)

sum_medians = 0
sum_fixed = 0
invalids = []
for update in updates:
    valid = True
    for i, value in enumerate(update[::-1], start=1):  # 77,32,69,11,94,74,35
        for next_val in update[:-i]:
            try:
                if next_val in rule_dict[value]:
                    valid = False
                    break
            except KeyError:
                pass
    if valid:
        sum_medians += update[len(update)//2]
    else:
        invalids.append(update)

print(sum_medians)
swaps = 0
sum_fixed_medians = 0
for line in invalids:
    checked_values = set()
    for n in range(len(line)//2):             # we only need to run the sort N/2 times for some reason
        for i in range(len(line)-1, -1, -1):  # start at, end at index 0,
            new_dest = i
            for j in range(i-1, -1, -1):
                if line[j] in rule_dict[line[i]]:
                    new_dest = j
            checked_values.add(line[i])

            if new_dest != i:
                line.insert(new_dest, line.pop(i))
                swaps += 1

    sum_fixed_medians += line[len(line) // 2]

print(sum_fixed_medians)
print("Swaps", swaps)
