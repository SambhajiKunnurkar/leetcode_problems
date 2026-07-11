class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        rows = {}

        for r in range(n):
            row = tuple(grid[r])
            rows[row]= 1 + rows.get(row, 0)
        
        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            count += rows.get(col, 0)
            
        return count