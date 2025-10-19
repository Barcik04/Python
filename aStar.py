import heapq

with open("grid.txt") as f:
    grid = [list(map(int, l.split())) for l in f if l.strip()]

H, W = len(grid), len(grid[0])
print(H, W)

start = (H - 1, 0)   # bottom-left
goal  = (0, W - 1)   # top-right

def print_grid(g):
    for row in g:
        print(" ".join(str(x) for x in row))
    print()

def move(start, goal):
    frontier = []

    r, c = start
    grid[r][c] = "*"

    for dr, dc in [(0,1), (-1,0), (0,-1), (1,0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 5 and grid[nr][nc] != "*":
            heapq.heappush(frontier, ((-nc, nr), (nr, nc)))
    print_grid(grid)

    while frontier:
        _, (r, c) = heapq.heappop(frontier)
        if grid[r][c] == "*" or grid[r][c] == 5:
            continue
        grid[r][c] = "*"
        print(f"Move to: {(r, c)}")
        print_grid(grid)
        if (r, c) == goal:
            print("You’ve reached the goal at:", (r, c))
            return

        for dr, dc in [(0,1), (-1,0), (0,-1), (1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 5 and grid[nr][nc] != "*":
                heapq.heappush(frontier, ((-nc, nr), (nr, nc)))

    print("No way to reach the goal (frontier exhausted).")

move(start, goal)
