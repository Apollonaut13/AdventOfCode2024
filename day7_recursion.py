import re

with (open("inputs/day7.txt") as inputFile):
    lines = [list(map(int, re.findall("\d+", line)))
             for line in inputFile.read().split("\n")]


def do_math(numbers, operators):
    result = []
    if len(numbers) <= 1:
        return numbers

    head, tail = numbers[-1], numbers[:-1]

    tail = do_math(tail, operators)
    for n in tail:
        for op in operators:
            if op == '+':
                result.append(n + head)
            if op == '*':
                result.append(n * head)
            if op == '||':
                result.append(int(f"{n}{head}"))
    return result


calibration_result = 0
calibration_result_2 = 0
for desired_result, *nums in lines:
    # part 1
    if desired_result in do_math(nums, '+*'):
        calibration_result += desired_result
    # part 2
    if desired_result in do_math(nums, ['+', '*', '||']):
        calibration_result_2 += desired_result

print(calibration_result)
print(calibration_result_2)
