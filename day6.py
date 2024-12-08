import time
with (open("inputs/day6.txt") as inputFile):
    grid = [f"x{line}x" for line in inputFile.read().split("\n")]
    grid = ["x"*len(grid[0])] + grid + ["x"*len(grid[0])]

visited = set()
visited_2 = []
starting_x, starting_y = None, None
guard_x, guard_y = None, None
direction = "up"
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == "^":
            starting_x, starting_y = guard_x, guard_y = (c, r)

while grid[guard_y][guard_x] != "x":
    visited.add((guard_x, guard_y))
    if direction == "up":
        guard_y -= 1
        if grid[guard_y][guard_x] == "#":
            guard_y += 1
            direction = "right"

    if direction == "down":
        guard_y += 1
        if grid[guard_y][guard_x] == "#":
            guard_y -= 1
            direction = "left"

    if direction == "right":
        guard_x += 1
        if grid[guard_y][guard_x] == "#":
            guard_x -= 1
            direction = "down"

    if direction == "left":
        guard_x -= 1
        if grid[guard_y][guard_x] == "#":
            guard_x += 1
            direction = "up"

print(len(visited))

# this takes forever to run, but it does complete part 2
startTime = time.time()
loop_creating_obstacle_count = 0

for x, y in list(visited):
    # reset the guard position and direction, and the places we're visiting
    direction = 1
    loop_visited = {
        (x, y): [direction]
    }
    guard_x, guard_y = starting_x, starting_y

    original_line = grid[y]  # save original configuration
    # add the new obstacle at x, y we've visited before
    line_with_new_obstacle = list(grid[y])
    line_with_new_obstacle[x] = "#"
    grid[y] = "".join(line_with_new_obstacle)

    # check if the new obstacle creates a loop

    while True:
        loop_visited[(guard_x, guard_y, direction)] = True
        if direction == 1:
            guard_y -= 1
            if grid[guard_y][guard_x] == "#":
                guard_y += 1
                direction = 2

        elif direction == 2:
            guard_x += 1
            if grid[guard_y][guard_x] == "#":
                guard_x -= 1
                direction = 3

        elif direction == 3:
            guard_y += 1
            if grid[guard_y][guard_x] == "#":
                guard_y -= 1
                direction = 4

        elif direction == 4:
            guard_x -= 1
            if grid[guard_y][guard_x] == "#":
                guard_x += 1
                direction = 1

        # if it does loop, add one to the counter
        if loop_visited.get((guard_x, guard_y, direction)):
            loop_creating_obstacle_count += 1
            break

        if grid[guard_y][guard_x] == "x":
            break

    # place the original line back into grid and go to the next position
    grid[y] = original_line

print(time.time() - startTime)
print(loop_creating_obstacle_count)
