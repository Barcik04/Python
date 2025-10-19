import heapq, math


with open("grid.txt") as f:
    grid = [list(map(int, l.split())) for l in f if l.strip()]

H, W = len(grid), len(grid[0])
start = (H - 1, 0)
goal  = (0, W - 1)


def print_grid(g):
    for row in g:
        print(" ".join(str(x) for x in row))
    print()


def move(start, goal):
    def h(r, c):
        return math.hypot(r - goal[0], c - goal[1])


    undiscovered_cells = []             # lista pól które nie zostały jeszcze odwiedzone, a czekają w kolejce
    total_cost = {start: 0}       # cena podróży od startu do danego pole
    came_from = {}            # to reconstruct the final path


    heapq.heappush(undiscovered_cells, (h(*start), start))


    while undiscovered_cells:
        f, (r, c) = heapq.heappop(undiscovered_cells)  # wybiera pole z najmniejszą hypot

        # jeśli dotarliśmy do końca
        if (r, c) == goal:
            # rekonstruujemy droge
            path = []
            cur = goal
            while cur != start:
                path.append(cur)
                cur = came_from[cur]
            path.append(start)
            path.reverse()

            for pr, pc in path:
                if grid[pr][pc] != 5:
                    grid[pr][pc] = "*"

            print_grid(grid)
            return path


        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # orientacja prawo lewo dół góra
            nr, nc = r + dr, c + dc  # coordynaty sąsiadujących pól

            # jesli sąsiedzi są poza mapą albo pole jest ścianą (5) to pomiń
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if grid[nr][nc] == 5:
                continue

            # ilosc pol przebytych do tego momentu
            new_cost = total_cost[(r, c)] + 1

            # Gdy nowa droga jest tansza to aktualizujemy ją
            if new_cost < total_cost.get((nr, nc), math.inf):
                total_cost[(nr, nc)] = new_cost
                came_from[(nr, nc)] = (r, c)

                # całkowita cena + metryka euklidosowska
                f_score = new_cost + h(nr, nc)
                heapq.heappush(undiscovered_cells, (f_score, (nr, nc)))

    return None



move(start, goal)
