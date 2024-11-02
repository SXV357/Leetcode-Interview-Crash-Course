from collections import deque
from typing import List, Set, Tuple

class MartianRiceSolver:
    def __init__(self):
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def find_connected_component(self, grid: List[List[int]], start_x: int, start_y: int, 
                               visited: Set[Tuple[int, int]]) -> Tuple[Set[Tuple[int, int]], bool]:
        """
        Find all connected cells of equal height and determine if water can escape.
        Returns: (component cells, can_escape)
        """
        rows, cols = len(grid), len(grid[0])
        height = grid[start_y][start_x]
        component = set()
        queue = deque([(start_x, start_y)])
        can_escape = False
        
        while queue:
            x, y = queue.popleft()
            if (x, y) in component:
                continue
                
            component.add((x, y))
            visited.add((x, y))
            
            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                
                if not (0 <= new_x < cols and 0 <= new_y < rows):
                    continue
                
                # If we find a lower height, water can escape
                if grid[new_y][new_x] < height:
                    can_escape = True
                    continue
                
                # If same height and not visited, add to queue
                if grid[new_y][new_x] == height and (new_x, new_y) not in component:
                    queue.append((new_x, new_y))
        
        return component, can_escape

    def count_rice_growing_areas(self, grid: List[List[int]]) -> int:
        """Count cells where water can pool using connected components approach."""
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = set()
        pooling_cells = 0
        
        # Process cells in descending order of height for efficiency
        height_cells = []
        for y in range(rows):
            for x in range(cols):
                height_cells.append((grid[y][x], x, y))

        # print(f"height cells: {height_cells}")

        height_cells.sort(reverse=True)
        # print(f"height cells: {height_cells}")
        
        for height, x, y in height_cells:
            if (x, y) in visited:
                continue
            
            # Find all connected cells of the same height
            print(f"x, y representing (column, row): {(x, y)}")
            component, can_escape = self.find_connected_component(grid, x, y, visited)
            print(f"component: {component}, can_escape: {can_escape}")
            
            # If water can't escape from this component, all cells in it can pool
            if not can_escape:
                pooling_cells += len(component)
        
        return pooling_cells

def main():
    # Read dimensions
    # x, y = map(int, input().split())
    x, y = 4, 3

    # Read grid row by row
    grid = [[0, 0, 4, 3], [0, 2, 2, 3], [2, 1, 4, 3]]
    # for _ in range(y):
    #     row = list(map(int, input().split()))
    #     grid.append(row)
    
    # Solve and output result
    solver = MartianRiceSolver()
    result = solver.count_rice_growing_areas(grid)
    print(result)

if __name__ == "__main__":
    main()