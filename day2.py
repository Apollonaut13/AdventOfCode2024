with open("inputs/day2.txt", 'r') as inputFile:
    rows = inputFile.read().split('\n')


def is_safe(r):
    safe, increasing, decreasing = True, False, False
    for i in range(len(r) - 1):
        diff = r[i + 1] - r[i]
        if abs(diff) > 3 or (diff == 0) or (diff > 0 and decreasing) or (diff < 0 and increasing):
            safe = False
            break
        increasing |= diff > 0
        decreasing |= diff < 0

    return safe


# part 1

safe_rows = 0
for row in rows:
    ints = [int(n) for n in row.split()]
    safe_rows += 1 if is_safe(ints) else 0
print(safe_rows)

# part 2

unsafe_rows_with_1_error = 0
for row in rows:
    ints = [int(n) for n in row.split()]
    if not is_safe(ints):
        safe_after_1_removal = False
        for i in range(len(ints)):
            new_ints = ints[::]
            new_ints.pop(i)
            if is_safe(new_ints):
                safe_after_1_removal = True

        if safe_after_1_removal:
            unsafe_rows_with_1_error += 1

print(safe_rows + unsafe_rows_with_1_error)
