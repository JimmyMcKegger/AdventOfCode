# Advent of code 2015 day 6 part 1
import numpy as np
import re


class Lights:
    def __init__(self):
        self.grid = np.zeros((1000, 1000), dtype=int)

    # iterate over the arrays switching all lights on
    def on(self, x1, y1, x2, y2):
        self.grid[x1 : x2 + 1, y1 : y2 + 1] = 1

    def off(self, x1, y1, x2, y2):
        self.grid[x1 : x2 + 1, y1 : y2 + 1] = 0

    # iterate over the arrays toggling all lights on or off
    def toggle(self, x1, y1, x2, y2):
        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                self.grid[i, j] = 1 if self.grid[i, j] == 0 else 0

    def b_on(self, x1, y1, x2, y2):
        self.grid[x1 : x2 + 1, y1 : y2 + 1] += 1

    def b_off(self, x1, y1, x2, y2):
        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                self.grid[i, j] -= 1 if self.grid[i, j] > 0 else 0

    # iterate over the arrays toggling all lights on or off
    def b_toggle(self, x1, y1, x2, y2):
        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                self.grid[i, j] += 2

    def count_on(self):
        return self.grid.sum()


def main():
    # load input into memory
    with open("input.txt") as f:
        contents = f.readlines()

    a = Lights()
    b = Lights()
    for line in contents:
        order = re.search(r"((toggle)|(on)|(off))", line)
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        
        eval(f"a.{order.group(1)}({x1},{y1},{x2},{y2})")
        eval(f"b.b_{order.group(1)}({x1},{y1},{x2},{y2})")

    print(f"Part 1: {a.count_on()}")
    print(f"Part 2: {b.count_on()}")


if __name__ == "__main__":
    main()
