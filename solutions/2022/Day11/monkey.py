# Advent of code 2022 Day 11


class Monkey:
    def __init__(self, id, items, operation, d, t, f):
        self.id = id
        self.inspect_count = 0
        self.items = items
        self.operation = operation
        self.divisor = int(d)
        self.true = int(t)
        self.false = int(f)

    def __repr__(self):
        return f"Monkey {self.id}, holding {self.items}, Inspect count of : {self.inspect_count}"

    def inspect_item(self, x):
        old = x
        new = eval(self.operation)
        self.inspect_count += 1
        relived_third = new // 3
        next_monkey = self.true if new % self.divisor == 0 else self.false
        return relived_third, next_monkey


def main():
    # open file
    with open("input.txt") as f:
        monkeys = f.read().split("\n\n")

    # make monkey list
    all_monkeys = []
    for index, monkey in enumerate(monkeys):
        ml = monkey.splitlines()
        items = list(map(int, ml[1][18:].split(", ")))
        inspect_operation = ml[2][18:]
        divisor = ml[3][21:]
        t = ml[4][29:]
        f = ml[5][30:]
        m = Monkey(index, items, inspect_operation, divisor, t, f)
        all_monkeys.append(m)

    # take turns
    for i in range(20):
        for monk in all_monkeys:
            for i in range(len(monk.items)):
                old = monk.items.pop(0)
                new_val, send_to = monk.inspect_item(old)
                all_monkeys[send_to].items.append(new_val)

    all_counts = []
    for m in all_monkeys:
        all_counts.append(m.inspect_count)
    all_counts.sort()
    print(f"Monkey business: {all_counts[-1] * all_counts[-2]}")


if __name__ == "__main__":
    main()
