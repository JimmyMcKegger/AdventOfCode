# Advent of code 2015 day 8
FILE = "input.txt"

def count_characters():
  counter = 0
  with open(FILE, "rb") as binf:
    contents = binf.readlines()
  for line in contents:
    for char in line:
      if char != 10:
        counter += 1
  return counter

def count_memory():
  count = 0
  with open(FILE, "rt") as memf:
    contents = memf.readlines()
  for line in contents:
    line = eval(line)
    count += len(line)
  return count

def encode_characters():
  counter = 0
  with open(FILE, "rt") as codf:
    contents = codf.readlines()
  for line in contents:
    # remove new line
    line = line.strip()
    # count opening and closing quotation marks
    counter += 2
    for c in line:
      # count double for escaped chars
      if c in ['\\', '"']:
        counter += 2
      else:
        counter += 1
  return counter

def part_one():
  chars = count_characters()
  mem = count_memory()
  diff1 = chars - mem
  print(f"Part one: {diff1}")

def part_two():
  chars = count_characters()
  encoded = encode_characters()
  diff2 = encoded - chars
  print(f"Part two: {diff2}")
  
if __name__ == "__main__":
  part_one()
  part_two()
