import re

# I ended up completely rewriting this code with recursion after taking a shower and thinking about it

with (open("inputs/day7.txt") as inputFile):
    lines = [list(map(int, re.findall("\d+", line)))
             for line in inputFile.read().split("\n")]


def valid_part1(desired_result, nums):
    operators = "+"*(len(nums)-1)

    for count in range(2**(len(operators))):
        binary_string = str(bin(count))[2:]
        ops = "".join("+*"[int(i, 2)] for i in binary_string)
        if len(ops) < len(nums)-1:
            ops = f"{'+'*(len(nums)-len(ops)-1)}{ops}"

        acc = nums[0]
        for i, op in enumerate(ops):
            if op == "+":
                acc += nums[i+1]

            if op == "*":
                acc *= nums[i+1]

            if acc == desired_result:
                # print(nums)
                # print(ops)
                # print("".join(f"{nums[i]}{ops[i]}" for i in range(len(ops)))+str(nums[-1]), "=", desired_result)
                return desired_result
    return 0


def ternary_string(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


def valid_part2(desired_result, nums):
    operators = "+"*(len(nums)-1)
    original_nums = nums[:]
    for count in range(3**len(operators)):
        nums = original_nums[:]
        ternary = ternary_string(count)
        ops = "".join("+*|"[int(i)] for i in ternary)
        """
        2|1|1+4+5
        211+4+5
        """
        if "|" in ops:
            math = "".join(f"{nums[i]}{ops[i]}" for i in range(len(ops)))+str(nums[-1])
            new_math = "".join(c for c in math if c != "|")
            nums = list(map(int, re.findall("\d+", new_math)))
            ops = "".join(c for c in ops if c != "|")

        if len(ops) < len(nums)-1:
            ops = f"{'+'*(len(nums)-len(ops)-1)}{ops}"

        acc = nums[0]
        for opIndex, op in enumerate(list(ops)):
            if op == "+":
                acc += nums[opIndex + 1]
            if op == "*":
                acc *= nums[opIndex + 1]

            if acc == desired_result:
                print("".join(f"{nums[i]}{ops[i]}" for i in range(len(ops)))+str(nums[-1]), "=", desired_result)
                return desired_result
    return False


calibration = 0
for result, *rest in enumerate(lines):
    calibration += valid_part1(result, rest)
print(calibration)
