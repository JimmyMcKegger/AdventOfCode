
INPUT_FILE = "input.txt"

def houses(d, x, y):
  if d == '^':
    y += 1
  elif d == '>':
    x += 1
  elif d == 'v':
    y -= 1
  else: 
    x -= 1
  return (x, y)

def main():
  with open(INPUT_FILE) as f:
        directions = list(f.read())

  x, y, robo_x, robo_y = 0, 0, 0, 0
  houses_visited = {(x,y)}
  for index, d in enumerate(directions):
    if index % 2 == 0:
      x, y = houses(d, x, y)
      houses_visited.add((x,y))
    else:
      robo_x, robo_y = houses(d, robo_x, robo_y)
      houses_visited.add((robo_x,robo_y))    

  print(f"{len(houses_visited)}")


if __name__ == "__main__":
  main()