def concat(A, B):
    return A + B

def generateSubsets(A: list[int], n: int, C: list[int]):
    if n == 0:
        return [C]

    excluding = generateSubsets(A, n - 1, C)
    including = generateSubsets(A, n - 1, concat(C, [A[n - 1]]))
    return concat(excluding, including)

# print(generateSubsets([1, 2, 3, 4], 3, []))

def countingSortByChar(arr, d):
    C = [0] * 26
    n = len(arr)

    for i in range(n):
        target = arr[i][2 - d]
        C[ord(target) - 65] += 1
    
    for j in range(1, 26):
        C[j] += C[j - 1]
    
    res = [0] * n
    
    for k in range(n - 1, -1, -1):
        target = arr[k][2 - d]
        res[C[ord(target) - 65] - 1] = arr[k]
        C[ord(target) - 65] -= 1
    
    return res

def sort_strings(arr, d):
    for i in range(d):
        arr = countingSortByChar(arr, i)
    
    return arr

print(sort_strings(["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA",
"NOW", "FOX"], 3))