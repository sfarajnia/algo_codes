import numpy as np

def median_of_three(l,r):
    m = (r-l) // 2 + l
    i = np.median([A[l-1], A[m-1], A[r-1]])
    if i == A[l-1]: return 1
    if i == A[m-1]: return m-l+1
    if i == A[r-1]: return r-l+1


def quick_sort(l, r, pivot):
    if r==-1: r=len(A)
    comparisons = np.max([0, r-l])
    if l >= r: return comparisons
    if pivot == -1:
        p = r 
    else:
        p = np.min([l + pivot - 1, r]) 
    A[l-1] , A[p-1] = A[p-1], A[l-1]
    i = l + 1
    for j in range(l+1, r+1):
        if A[l-1] > A[j-1]:
            A[i-1], A[j-1] = A[j-1], A[i-1]
            i += 1
    A[i-2] , A[l-1] = A[l-1], A[i-2]
    # comparisons += quick_sort(l, i-2, -1)
    # comparisons += quick_sort(i , r, -1)
 
    comparisons += quick_sort(l, i-2,
                              median_of_three(l, i-2))
    comparisons += quick_sort(i , r,
                              median_of_three(i, r))       
    return comparisons
        
# A = [1, 2, 3, 5, 4, 1, 9, 0, -1, 10]
# # A = list(range(100))
# # comparisons = quick_sort(1,-1, median_of_three(1, len(A)))
# comparisons = quick_sort(1,-1, 1)
# print(A, comparisons)

# A = np.random.randint(-20, 100, 100)
# comparisons = quick_sort(1,-1, 2)
# print(A, comparisons)

with open('integer_array_Qsort.txt') as int_file:
    int_list = []
    for line in int_file:
        int_list.append(int(line))

A = int_list
# comparisons = quick_sort(1,-1, -1)
# comparisons = quick_sort(1,-1, 1)
comparisons = quick_sort(1,-1,
                         median_of_three(1, len(A)))
print(A, comparisons)