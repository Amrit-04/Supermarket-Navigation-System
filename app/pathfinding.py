import csv
from heapq import heappush, heappop

# Load grid from CSV file
def load_grid_from_csv(file_path="app/grid.csv"):
    with open(file_path, newline='', encoding='utf-8-sig') as f:  # <-- use utf-8-sig
        reader = csv.reader(f)
        return [[int(cell) for cell in row] for row in reader]

# A* pathfinding algorithm
def a_star(start, goal, grid):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        x, y = current
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # 4 directions
            neighbor = (x+dx, y+dy)
            if (
                0 <= neighbor[0] < len(grid[0]) and
                0 <= neighbor[1] < len(grid) and
                grid[neighbor[1]][neighbor[0]] != 1
            ):
                temp_g = g_score[current] + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current
    return []
