import pandas as pd
import heapq

FILE = "input.txt"

with open(FILE) as f:
  lines = f.read().splitlines()

grid_one = pd.array(lines)

x = len(grid_one[0])
y = len(grid_one)

start = end = ''
while not start and not end:
  for i in range(y):
    for j in range(x):
      if grid_one[i][j] == 'S':
        #print("Found Start")
        start = [i,j]
      if grid_one[i][j] == 'E':
        #print("Found End")
        end = [i,j]
        
def height(char):
  if char == 'S':
    return 0
  elif char == 'E':
    return 27
  else:
    return ord(char) - 96

def new_height(char):
  if char == 'S':
    return 1
  elif char == 'E':
    return 27
  else:
    return ord(char) - 96

def moves(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        next_i = i + di
        next_j = j + dj

        if not (0 <= next_i < y and 0 <= next_j < x):
            continue

        if height(grid_one[next_i][next_j]) <= height(grid_one[i][j]) + 1:
            yield next_i, next_j

def moves_backwards(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        next_i = i + di
        next_j = j + dj

        if not (0 <= next_i < y and 0 <= next_j < x):
            continue

        if height(grid_one[next_i][next_j]) >= height(grid_one[i][j]) - 1:
            yield next_i, next_j

# make a priority queue
visited = pd.array([[False] * x for _ in range(y)])
heap = [(0, start[0], start[1])]
while True:
    steps, this_i, this_j = heapq.heappop(heap)

    if visited[this_i][this_j]:
        continue
    visited[this_i][this_j] = True
    
    if [this_i, this_j] == end:
        print(f"Shortest path from `S` to the top is {steps} steps")
        break

    for next_i, next_j in moves(this_i, this_j):
        heapq.heappush(heap, (steps + 1, next_i, next_j))


# part 2 go backwards

grid_two = pd.array(lines)

x = len(grid_two[0])
y = len(grid_two)

starts = []
end = []
for i in range(y):
  for j in range(x):
    if grid_two[i][j] in ['a', 'S']:
      starts.append([i,j])
    if grid_two[i][j] == 'E':
      #print("Found End")
      end = [i,j]

# make another priority queue
visited_two = pd.array([[False] * x for _ in range(y)])
heap_two = [(0, end[0], end[1])]
while True:
    steps, this_i, this_j = heapq.heappop(heap_two)
    #print(steps, this_i, this_j, grid_two[this_i][this_j])

    if visited_two[this_i][this_j]:
        continue
    visited_two[this_i][this_j] = True
    
    if new_height(grid_two[this_i][this_j]) == 1:
        print(f"Shortest path from `E` to the bottom is {steps} steps")
        break

    for next_i, next_j in moves_backwards(this_i, this_j):
        heapq.heappush(heap_two, (steps + 1, next_i, next_j))
