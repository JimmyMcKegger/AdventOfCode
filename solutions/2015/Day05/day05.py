"""
Finds a nice string for :
https://adventofcode.com/2015/day/5
"""
import re

def no_disallowed(str):
  disallowed = ['ab', 'cd', 'pq', 'xy']
  func = lambda char : char not in str
  return all(map(func, disallowed))

def part_1(list):
  match_count = 0
  #  for each line check for a match
  for line in list:
    # make sure there's no ab, cd, pq, or xy.
    if no_disallowed(line):
      #  has 3 vowels
      if re.match(r"(\w*[aeuio]\w*){3,}", line):
        # at least one letter that appears twice in a row
        if re.search(r"(.)\1",line):
          match_count += 1
  return f"Part one total: {match_count}"

def part_2(list):
  second_match_count = 0
  #  for each line check for a match
  for line in list:
    # pair of any two letters that appears at least twice in the string without overlapping
    if re.search(r"(.)(.).*\1\2", line):
      #  contains at least one letter which repeats with exactly one letter between them
      if re.search(r"(.).\1", line):
        second_match_count += 1
  return f"Part two total: {second_match_count}"

def main():
  # load the strings from input.txt
  with open("input.txt") as f:
    santas_list = f.readlines()
  print(part_1(santas_list))
  print(part_2(santas_list))
  exit(0)
  
if __name__ == "__main__":
  main()