"""
PassingCars
Count the number of passing cars on the road.

A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:
class Solution { public int solution(int[] A); }
that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.


[0 1 1 0 1]
(0, 1) -->
0, 1
0, 2
0, 4
3, 4

input:
an array of integers

output:
count number of pairs 0,1

conditions:
-1 if number of pairs > 1000000000
"""


def passing_cars(A):
    pairs = []
    pairs_indexs = []

    for i, a in enumerate(A):
        for j in range(i + 1, len(A)):
            if a == 0 and A[j] == 1:
                pairs_indexs.append((i, j))
                pairs.append((a, A[j]))
    print(pairs)
    print(pairs_indexs)

    # complexity would be: O(N**2)
    # try to make it to be: O(N)

    # pairs = []
    # for i in range(len(A)):
    #     pairs += list(zip(A[i:], A[i + 1 :]))
    # pairs = [pair for pair in pairs if pair == (0, 1)]
    # print(pairs)


passing_cars([0, 1, 0, 1, 1])
