# Advent of code 2015 day 2, part 2 ribbon 
import re
INPUT_FILE = "input.txt"

def get_total_ribbon(arr):
  l, w, h = arr  
  bow = l * w * h
  arr.sort()
  shortest_double = arr[0]*2
  next_shortes_double = arr[1]*2
  side_ribbon = shortest_double + next_shortes_double
  return side_ribbon + bow


def main():
  with open(INPUT_FILE) as f:
    lines = f.readlines()

  all_gifts = []
  for line in lines:
    line = list(map(int,re.findall(r'\d+', line)))
    all_gifts.append(line)
  
  total_ribbon = []
  for gift in all_gifts:
    total_ribbon.append(get_total_ribbon(gift))

  print(sum(total_ribbon))
  

if __name__ == "__main__":
  main()