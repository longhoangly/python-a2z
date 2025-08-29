"""
A[0] = 4
A[1] = 1
A[2] = 3
A[3] = 2
return 1

A[0] = 4
A[1] = 1
A[2] = 3
return 0

input: arrayA which has N integers
output: 1 if arrayA is permutation, 0 if arrayA is not permutation
condition: check if elements from 1-N appeared in A once only
"""


def permutation(A):
    # n = len(A)
    # for i in range(1, n + 1):
    #     appears_in_array = A.count(i)
    #     if appears_in_array > 1 or appears_in_array == 0:
    #         return 0
    # return 1

    n = len(A)
    set_a = set(A)
    if len(A) == len(set_a) and max(set_a) == n and min(set_a) == 1:
        return 1
    else:
        return 0


print(permutation([1, 2, 3, 4]))
print(permutation([1, 3, 4]))
print(permutation([1, 1, 2, 3, 4]))
print(permutation([2, 3, 4, 5]))
