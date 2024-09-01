def concat(A, B):
    return A + B

def generateSubsets(A: list[int], n: int, C: list[int]):
    if n == 0:
        return [C]

    excluding = generateSubsets(A, n - 1, C)
    including = generateSubsets(A, n - 1, concat(C, [A[n - 1]]))
    return concat(excluding, including)

print(generateSubsets([1, 2, 3, 4], 3, []))