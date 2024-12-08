import time
import timeit

with open("inputs/day1.txt", 'r') as inputFile:
    rows = inputFile.read().split('\n')

# part 1

leftList = []
rightList = []
for row in rows:
    left, right = [int(n) for n in row.split()]
    leftList.append(left)
    rightList.append(right)

leftList.sort()
rightList.sort()

totalDistance = sum(abs(left - right) for left, right in list(zip(leftList, rightList)))
print(totalDistance)

# part 2

print(sum(n * rightList.count(n) for n in leftList))
