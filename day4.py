with open("inputs/day4.txt", "r") as inputFile:
    lines = inputFile.read().split("\n")

# part 1

horiz, verts = 0, 0
cols = [""]*len(lines)
for i, row in enumerate(lines):
    horiz += row.count("XMAS") + row.count("SAMX")
    for j, c in enumerate(row):
        cols[j] += c

for col in cols:
    verts += col.count("XMAS") + col.count("SAMX")

diags = 0
for lineIndex, line in enumerate(lines):
    if lineIndex > len(lines)-4:
        break
    for colIndex in range(len(line) - 3):
        if lines[lineIndex][colIndex] in "SX":
            downRight = "".join(lines[lineIndex+n][colIndex+n] for n in range(4))
            if downRight in {"XMAS", "SAMX"}:
                diags += 1
    for colIndex in range(3, len(line)):
        if lines[lineIndex][colIndex] in "SX":
            downLeft = "".join(lines[lineIndex+n][colIndex-n] for n in range(4))
            if downLeft in {"XMAS", "SAMX"}:
                diags += 1

print(horiz + verts + diags)

# part 2
xmases = 0
for rowIndex, line in enumerate(lines):
    for colIndex, c in enumerate(line):
        if c == "A":
            try:
                surrounds = lines[rowIndex-1][colIndex-1] + \
                            lines[rowIndex-1][colIndex+1] + \
                            lines[rowIndex+1][colIndex-1] + \
                            lines[rowIndex+1][colIndex+1]
                if surrounds in {"SSMM", "MMSS", "MSMS", "SMSM"}:
                    xmases += 1
            except IndexError:
                pass

print(xmases)
