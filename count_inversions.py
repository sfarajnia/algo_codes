'''
to count the inversions in an array, i will use merge-sort.
I will sort and count inversions in subproblems.
sorting subproblems helps to do the merge step in
O(n)
'''


import numpy as np

def  merge_count(A, B):
    M = []
    inversions = 0
    i = j = 0
    while (i < len(A) and j < len(B)):
        if A[i] <= B[j]:
            M.append(A[i])
            i += 1
        else:
            M.append(B[j])
            inversions += len(A) - i
            j += 1
    if i == len(A):
        M.extend(B[j:])
    else:
        M.extend(A[i:])
    return M, inversions


def count_merge_sort(L):
    if len(L) == 1: return L, 0
    A, inversions_A = count_merge_sort(L[:len(L)//2])
    B, inversions_B = count_merge_sort(L[len(L)//2:])
    M, inversions = merge_count(A, B)
    return M, inversions+inversions_A+inversions_B

L = [1, 2, 3, 5, 4, 1, 9, 0, -1, 2] 
print(count_merge_sort(L)) #inversions should be 24


L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
print(count_merge_sort(L)) #inversions should be 45

# L = np.random.randint(-20, 100, 100)
# print(merge_sort(L))
with open('integer_array.txt') as int_file:
    int_list = []
    for line in int_file:
        int_list.append(int(line))

print(count_merge_sort(int_list)[1])   