class Solution:
    def depthFirstSearch(self, matrix, r, c, row_size, col_size, visited):
        visited[r][c] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            new_row, new_col = r + dx, c + dy
            if new_row in range(row_size) and new_col in range(col_size) and matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
                self.depthFirstSearch(matrix, new_row, new_col, row_size, col_size, visited)

    def countIslands(self, matrix):
        row_size = len(matrix)
        col_size = len(matrix[0])
        visited = [[False] * col_size for _ in range(row_size)]

        count_island = 0
        for r in range(row_size):
            for c in range(col_size):
                if matrix[r][c] == 1 and not visited[r][c]:
                    count_island += 1
                    self.depthFirstSearch(matrix, r, c, row_size, col_size, visited)

        return count_island

# Example Usage
matrix = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0]
]

solution = Solution()
result = solution.countIslands(matrix)
print(result)
