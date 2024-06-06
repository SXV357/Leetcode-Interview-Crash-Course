# 2352

from collections import defaultdict

def equalPairs(grid: list[list[int]]) -> int:
    """
    Time complexity: O(n^2) because for updating the result we are iterating through all columns of the matrix for all the `n x n` values
    Space complexity: O(n) because if all the rows are unique the dictionary stores `n` keys
    """
    # Brute force solution - Accepted because of the small input constraints(will give TLE for larger inputs)
        # Accumulates all the rows and all the columns and compares pairs to see which ones match

    # rows, cols = [], []

    # for row in grid:
    #     rows.append(row)
    
    # for i in range(len(grid[0])):
    #     curr = []
    #     for j in range(len(grid)):
    #         curr.append(grid[j][i])
    #     cols.append(curr)
    
    # res = 0
    # for r in rows:
    #     for c in cols:
    #         if r == c:
    #             res += 1
    
    # return res

    # More optimal solution using a hashmap

    mappings = defaultdict(int) # this map is used to map each row ONLY in the matrix to its frequency

    # the logic below is used to update the matrix but the only thing that needs to be taken into account is that dictionary keys need to be immutable and arrays are mutable so we need to convert it to a tuple for it to work
    for row in grid:
        mappings[tuple(row)] += 1

    # we first get all the values in a given column and store it in an array given by the variable curr
    for i in range(len(grid[0])):
        curr = []
        for j in range(len(grid)):
            curr.append(grid[j][i])
        
        # if we have encountered a column which matches an existing row then the reason why we increment the answer by the frequency of the row is that if for example the row that it matches occurs n times in the matrix then there are n possible combinations involving those rows with this column and this logic carries forward for the other columns
        if tuple(curr) in mappings:
            res += mappings[tuple(curr)]
    
    return res

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))