def countingSortBySegment(A, segment):
    C = [0] * 256
    n = len(A)

    for i in range(n):
        components = A[i].split(".")
        C[int(components[4 - segment - 1])] += 1
    
    for j in range(1, 256):
        C[j] += C[j - 1]
    
    res = [0] * n
    for k in range(n - 1, -1, -1):
        components = A[k].split(".")
        value = int(components[4 - segment - 1])
        res[C[value] - 1] = A[k]
        C[value] -= 1
    
    for x in range(len(res)):
        A[x] = res[x]

def sortIP(A, segments):
    for segment in range(segments):
        countingSortBySegment(A, segment)
    
    return A

arr = ["192.168.100.1", "8.8.8.8", "0.0.0.000", "127.0.1.1", "10.0.0.1", "127.0.0.1"]

def getSegment(ip: str, d: int):
    segments = ip.split(".")
    return int(segments[d])

def modifiedCountingSortBySegment(A, d):
    C = [[] for _ in range(256)]

    for ip in A:
        segment = getSegment(ip, d)
        C[segment].append(ip)
    
    B = []
    for i in range(256):
        if C[i]:
            for el in C[i]:
                B.append(el)
    
    return B

def modified_sort(A, n):
    for d in range(n - 1, -1, -1):
        A = modifiedCountingSortBySegment(A, d)
    
    return A

res = modified_sort(arr, 4)
print(res)