# Advent of code 2015 day 2 wrapping paper
import re

def get_total(arr):
  l, w, h = arr
  cover = 2*l*w + 2*w*h + 2*h*l
  arr.sort()
  slack = arr[0] * arr[1]
  total = cover + slack
  return total

def main():
  with open("input.txt") as f:
    lines = f.readlines()

  all_gifts = []
  for line in lines:
    line = list(map(int,re.findall(r'\d+', line)))
    all_gifts.append(line)
  
  total_paper = []
  for gift in all_gifts:
    total_paper.append(get_total(gift))

  print(sum(total_paper))
  
  
if __name__ == "__main__":
  main()