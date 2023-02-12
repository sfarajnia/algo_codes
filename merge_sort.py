import numpy as np

def  merge(A, B):
    M = []
    i = j = 0
    while (i < len(A) and j < len(B)):
        if A[i] < B[j]:
            M.append(A[i])
            i += 1
        else:
            M.append(B[j])
            j += 1
    if i == len(A):
        M.extend(B[j:])
    else:
        M.extend(A[i:])
    return M


def merge_sort(L):
    if len(L) == 1: return L
    A = merge_sort(L[:len(L)//2])
    B = merge_sort(L[len(L)//2:])
    return merge(A, B)

L = [1, 2, 3, 5, 4, 1, 9, 0, -1, 2]
print(merge_sort(L))

L = np.random.randint(-20, 100, 100)
print(merge_sort(L))