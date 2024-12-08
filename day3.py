import re
with open("inputs/day3.txt", "r") as inputFile:
    memory = inputFile.read()
    do_memory = memory.split("don't()")


def apply_multipliers(s: str):
    return sum(int(left)*int(right) for left, right in re.findall("mul\((\d+),(\d+)\)", s))


# part 1
print(apply_multipliers(memory))

# part 2
sum_dos = apply_multipliers(do_memory[0])
for line in do_memory[1:]:
    if "do()" in line:
        split_line = "".join(line.split('do()')[1:])
        sum_dos += apply_multipliers(split_line)
print(sum_dos)
