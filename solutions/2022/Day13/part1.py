FILE = "input.txt"

def compare(l, r):
  l_len = len(l)
  r_len = len(r)
  max_len = max(l_len, r_len)

  for i in range(max_len):
    if i >= l_len:
      return 1

    if i >= r_len:
      return 0

    left = l[i]
    right = r[i]

    ordered = -1
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            ordered = 1
        elif left > right:
            ordered = 0
        else:
            ordered = -1
            continue

    elif isinstance(left, list) and isinstance(right, list):
        ordered = compare(left, right)
    elif isinstance(left,list) and isinstance(right, int):
        right = [right]
        ordered = compare(left, right)
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        ordered = compare(left, right)
    if ordered != -1:
        return ordered
  return -1
    
  for index, value in enumerate(l):
    if isinstance(l, list) and isinstance(r, list):
      compare(l[0])
    if isinstance(l, int):
      compare(l, r[index:])
    if value < r[index]:
      count_ordered += 1
      break

def main():
  with open(FILE) as f:
    data = f.read().split("\n\n")

  ordered_indices = []
  for pair in data:
    l, r = pair.split("\n")
    l = eval(l)
    r = eval(r)
    ordered_indices.append(compare(l, r))

  total = 0
  for ind, val in enumerate(ordered_indices):
    if val == 1:
      total += ind + 1

  print(f"Part 1: total of {total}")

if __name__ == "__main__":
  main()
