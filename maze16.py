import numpy as np
import random

N = 16
m = np.arange(1, N*N + 1).reshape(N, N)
print(m)
# generate random blocked cells
b = 20
block_cells = set()
while len(block_cells) < b:
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)
    block_cells.add((i, j))

#start and end are not blocked
block_cells.discard((0, 0))
block_cells.discard((15, 15))

print("\nMaze view (██ = blocked):")
for i in range(N):
    row = ""
    for j in range(N):
        if (i, j) in block_cells:
            row += "██ "
        else:
            row += f"{m[i, j]:3d} "
    print(row)

start = (0, 0)
end   = (15, 15)

rows = N
cols = N

visited = np.zeros((N, N), dtype=int)

shortest_path = None
shortest_len  = float('inf')

def move(i, j, direction):
    if direction == "north": return i-1, j
    if direction == "south": return i+1, j
    if direction == "west":  return i, j-1
    if direction == "east":  return i, j+1
        
def search(i, j, path):
    global shortest_path, shortest_len
    
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return
    if (i, j) in block_cells:
        return
    if visited[i][j] == 1:
        return

    path.append((i, j))
    visited[i][j] = 1

    if (i, j) == end:
        if len(path) < shortest_len:
            shortest_len = len(path)
            shortest_path = path.copy()
        
        visited[i][j] = 0
        path.pop()
        return

    for direction in ["north", "south", "west", "east"]:
        i1, j1 = move(i, j, direction)
        search(i1, j1, path)

    visited[i][j] = 0
    path.pop()

search(start[0], start[1], [])

if shortest_path is None:
    print("No path found.")
else:
    print("Shortest path length:", shortest_len)
    print("Path:", shortest_path)

    path_numbers = [int(m[i, j]) for (i, j) in shortest_path]
    print("Path as cell numbers:", path_numbers)
