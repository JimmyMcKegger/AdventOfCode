INPUT_FILE = "input.txt"

def part_one():
  with open(INPUT_FILE) as f:
        input_list = list(map(int,f.read()))
  first = input_list[0]
  input_list.append(first)
  matches = []
  for index, val in enumerate(input_list[:-1]):
    if val == input_list[index + 1]:
      matches.append(val)
  ans = sum(matches)
  print(f"Part One: {ans}")

def part_two():
  with open(INPUT_FILE) as f:
        input_list = list(map(int,f.read()))
  starting_length = len(input_list)
  halfway_length = starting_length // 2
  input_list = input_list + input_list
  matches = []
  for index, val in enumerate(input_list[:starting_length]):
    if val == input_list[index + halfway_length]:
      matches.append(val)

  ans = sum(matches)
  print(f"Part two: {ans}")
  

if __name__ == "__main__":
  part_one()
  part_two()
