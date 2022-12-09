# Advent of code 2022 Day 9
import math


class Rope:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.knot1 = [0, 0]
        self.knot2 = [0, 0]
        self.knot3 = [0, 0]
        self.knot4 = [0, 0]
        self.knot5 = [0, 0]
        self.knot6 = [0, 0]
        self.knot7 = [0, 0]
        self.knot8 = [0, 0]
        self.visited_by_tail = {(0, 0)}
        self.visited_by_knot8 = {(0, 0)}

    def move(self, d, num):
        for _ in range(0, int(num)):
            if d == "U":
                self.head[1] += 1
            elif d == "D":
                self.head[1] -= 1
            elif d == "L":
                self.head[0] -= 1
            else:
                self.head[0] += 1

            # part 1
            self.tail_follow(self.head, self.tail, 1)
            # part 2
            self.tail_follow(self.tail, self.knot1, 0)
            self.tail_follow(self.knot1, self.knot2, 0)
            self.tail_follow(self.knot2, self.knot3, 0)
            self.tail_follow(self.knot3, self.knot4, 0)
            self.tail_follow(self.knot4, self.knot5, 0)
            self.tail_follow(self.knot5, self.knot6, 0)
            self.tail_follow(self.knot6, self.knot7, 0)
            self.tail_follow(self.knot7, self.knot8, 2)

    def tail_follow(self, h, t, to_update):
        # measure
        span = math.dist(h, t)

        if span >= 2.0:
            x_dif = h[0] - t[0]
            y_dif = h[1] - t[1]

            # diagonal
            if h[0] != t[0] and h[1] != t[1]:
                # up-right
                if x_dif > 0 and y_dif > 0:
                    t[0] += 1
                    t[1] += 1

                # down-right
                elif x_dif > 0 and y_dif < 0:
                    t[0] += 1
                    t[1] -= 1

                # up-left
                elif x_dif < 0 and y_dif > 0:
                    t[0] -= 1
                    t[1] += 1

                # down-left
                else:
                    t[0] -= 1
                    t[1] -= 1

            # perpendicular
            else:
                # right
                if x_dif >= 2:
                    t[0] += 1
                # left
                elif x_dif <= -2:
                    t[0] -= 1
                # up
                if y_dif >= 2:
                    t[1] += 1
                # down
                elif y_dif <= -2:
                    t[1] -= 1

            if to_update == 1:
                self.visited_by_tail.add(tuple(t))

            elif to_update == 2:
                self.visited_by_knot8.add(tuple(t))


if __name__ == "__main__":

    with open("input.txt") as f:
        moves = f.read().splitlines()

    r = Rope()
    for m in moves:
        d, n = m.split(" ")
        r.move(d, n)
    print(f"The tail visited {len(r.visited_by_tail)} spaces")
    print(f"The last knot visited {len(r.visited_by_knot8)} spaces")
