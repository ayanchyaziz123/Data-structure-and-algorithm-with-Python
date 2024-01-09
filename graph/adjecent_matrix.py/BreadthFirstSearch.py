
#find number of island
# 1 contains island and 0 contains water
# you can go four direction
class Solution:
    def breadthFirst_search(self, matrix, r, c, row_size, col_size, visited,):
        queue = []
        queue.append([r, c])
        visited[r][c] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            curr_row, curr_col = queue.pop(0)
            for dx, dy in directions:
                new_row = dx + curr_row
                new_col = dy + curr_col
                if new_row in range(row_size) and new_col in range(col_size) and matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    queue.append([new_row, new_col])
                    visited[new_row][new_col] = True
            
matrix = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0]
]

row_size = len(matrix)
col_size = len(matrix[0])
visited = [[False] * col_size for _ in range(row_size)]

count_island = 0
for r in range(row_size):
    for c in range(col_size):
        if matrix[r][c] == 1 and not visited[r][c]:
            count_island += 1
            Solution().breadthFirst_search(matrix, r, c, row_size, col_size, visited)
print(count_island)            