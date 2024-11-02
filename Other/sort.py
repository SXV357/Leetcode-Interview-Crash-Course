import math

def countingSortByDigit(A, currDigit) -> None:
    C = [0] * 8
    n = len(A)
    power = 10 ** currDigit

    for i in range(n):
        curr = math.floor(A[i] // power) % 10
        C[curr] += 1
    
    for j in range(1, 8):
        C[j] += C[j - 1]
    
    B = [0] * n
    for k in range(n - 1, -1, -1):
        digit = math.floor(A[k] // power) % 10
        B[C[digit] - 1] = A[k]
        C[digit] -= 1
    
    for x in range(len(B)):
        A[x] = B[x]

def octalSort(A, d):
    for currDigit in range(d):
        countingSortByDigit(A, currDigit)
    
    return A

arr = [346, 724, 145, 000, 0o001, 210]
res = octalSort(arr, 3)
print(res)