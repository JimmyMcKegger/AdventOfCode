import numpy as np


def view_calculate(viewpoint, above, below, left, right):
    above_count = below_count = left_count = right_count = 0
    for tree in above[::-1]:
        if tree < viewpoint:
            above_count += 1
            continue
        elif tree >= viewpoint:
            above_count += 1
            break
        else:
            break

    for tree in below[::-1]:
        if tree < viewpoint:
            below_count += 1
            continue
        elif tree >= viewpoint:
            below_count += 1
            break
        else:
            break

    for tree in left[::-1]:
        if tree < viewpoint:
            left_count += 1
            continue
        elif tree >= viewpoint:
            left_count += 1
            break
        else:
            break

    for tree in right:
        if tree < viewpoint:
            right_count += 1
            continue
        elif tree >= viewpoint:
            right_count += 1
            break
        else:
            break

    total = 1
    for view in [above_count, below_count, left_count, right_count]:
        total *= view

    return total


with open("input.txt") as f:
    data = f.read().split("\n")

grid = []
for line in data:
    line = list(line)
    num_line = []
    for char in line:
        num_char = int(char)
        num_line.append(num_char)
    grid.append(num_line)

w = len(grid[0])
h = len(grid)

arr = np.array(grid)

count = 0
viewscores = []
for y, row in enumerate(arr):
    if y == 0 or y == h - 1:
        count += w
        continue
    for a, b in enumerate(row):
        above = np.take(arr, a, axis=1)[:y]
        below = np.take(arr, a, axis=1)[y + 1 :]
        left = row[:a]
        right = row[a + 1 :]

        if a == 0 or a == w - 1:
            count += 1
            continue
        elif b > above.max():
            count += 1
            viewscores.append(view_calculate(b, above, below, left, right))
            continue
        elif b > below.max():
            count += 1
            viewscores.append(view_calculate(b, above, below, left, right))
            continue
        elif b > left.max():
            count += 1
            viewscores.append(view_calculate(b, above, below, left, right))
            continue
        elif b > right.max():
            count += 1
            viewscores.append(view_calculate(b, above, below, left, right))
            continue


if __name__ == "__main__":
    print(f"Final count visible form outsidez: {count}")
    print(f"Highest possible Scenic score: {max(viewscores)}")
