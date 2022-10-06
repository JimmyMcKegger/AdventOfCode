# AOC 2021 day 4
import re
INPUT_FILE = "day_4_input.txt"

class Num:
    def __init__(self, n):
        self.val = n
    
    def __repr__(self):
        return str(self.val)
    
    def __str__(self):
        return str(self.val)

class Board:
    def __init__(self, input_lines):
        self.total_value = 0
        self.tally_dict = {}
        self.current = 0
        self.board = [
            [],
            [],
            [],
            [],
            []
        ]
        index = 0
        for line in input_lines:
            arr = re.findall("\d{1,2}", line)
            new_arr = []
            for i in arr:
                new_arr.append(i)
                # build the board's total value when initialising
                self.total_value += int(i)
            self.board[index] = new_arr
            index += 1

    def __iter__(self):
        return self.board[self.current]

    def __next__(self):
        self.current += 1
        if self.current > 4:
            raise StopIteration
        return self.current

    def __repr__(self):
        return str(self.board)

    def __str__(self):
        return str(self.board)

def find_winner(g_nums, g_boards):
    for num in g_nums:
        for board in g_boards:
            board.current = 0
            line_count = 0
            for line in board.board:
                if num in line:
                    # print(f"found {num} in {board}")
                    # log the row in the tally dict
                    if f"Row {line_count}" in board.tally_dict:
                        board.tally_dict[f"Row {line_count}"] += 1
                    else:
                        board.tally_dict[f"Row {line_count}"] = 1
                    # log the column in the tally dict
                    if f"Column {line.index(num)}" in board.tally_dict:
                        board.tally_dict[f"Column {line.index(num)}"] += 1
                    else:
                        board.tally_dict[f"Column {line.index(num)}"] = 1
                    # subtract the num from the board's total
                    board.total_value -= int(num)
                    # print(f"TALLY: {board.tally_dict}")
                    if 5 in board.tally_dict.values():
                        return board.total_value * int(num)
                line_count += 1

def main():
    bingo = False
    game_boards = []
    
    with open(INPUT_FILE) as f:
        contents = f.readlines()
    game_numbers = contents[0].split(",")
    game_ints = list(map(int, game_numbers))

    board_contents = contents[2:]
    while len(board_contents) >= 5:
        new = Board(board_contents[:5])
        """ for line in new.board:
            print(line)
        print("\n") """
        game_boards.append(new)
        board_contents = board_contents[6:]
    
    winner_total = find_winner(game_numbers, game_boards)
    print(winner_total)


if __name__ == "__main__":
    main()
