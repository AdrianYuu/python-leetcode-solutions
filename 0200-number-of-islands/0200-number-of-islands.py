class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set() # (row, col)

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()

                # right, left, up, down
                directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

                for dy, dx in directions:
                    y = r + dy
                    x = c + dx

                    if (
                        y in range(rows) and
                        x in range(cols) and
                        grid[y][x] == "1" and
                        (y, x) not in visited
                    ):
                        q.append((y, x))
                        visited.add((y, x))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    result += 1

        return result