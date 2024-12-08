with open("inputs/day8.txt", "r") as inputFile:
    lines = [list(line) for line in inputFile.read().split("\n")]

antennae = dict()
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == ".":
            continue
        if antennae.get(char):
            antennae[char].append((r, c))
        else:
            antennae[char] = [(r, c)]

# part 1
anti_nodes_part1 = set()
for ID, locations in antennae.items():
    for nodeIndex, (AR, AC) in enumerate(locations):
        for BR, BC in locations[nodeIndex+1:]:
            antinode1 = (AR + 2*(BR-AR), AC + 2*(BC-AC))
            antinode2 = (BR + 2*(AR-BR), BC + 2*(AC-BC))

            if 0 <= antinode1[0] < len(lines) and 0 <= antinode1[1] < len(lines[0]):
                anti_nodes_part1.add(antinode1)
            if 0 <= antinode2[0] < len(lines) and 0 <= antinode2[1] < len(lines[0]):
                anti_nodes_part1.add(antinode2)

print(len(anti_nodes_part1))

# part 2
anti_nodes_part2 = set()
for ID, locations in antennae.items():
    for nodeIndex, (AR, AC) in enumerate(locations):
        for BR, BC in locations[nodeIndex+1:]:
            for mult in range(1, 27):  # the only change in part 2
                antinode1 = (AR + mult*(BR-AR), AC + mult*(BC-AC))  # apply multipliers
                antinode2 = (BR + mult*(AR-BR), BC + mult*(AC-BC))

                if 0 <= antinode1[0] < len(lines) and 0 <= antinode1[1] < len(lines[0]):
                    anti_nodes_part2.add(antinode1)
                if 0 <= antinode2[0] < len(lines) and 0 <= antinode2[1] < len(lines[0]):
                    anti_nodes_part2.add(antinode2)

print(len(anti_nodes_part2))
