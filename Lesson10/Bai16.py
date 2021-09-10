# /*
#     Đếm số lượng số chẵn trên biên của ma trận các số nguyên kích thượng MxN
# */
import math

import myfuntions


def solution(A):
    count = 0
    for i in range(0, len(A[0])):
        if A[0][i] % 2 == 0:
            count += 1
        if A[len(A) - 1][i] % 2 == 0 and len(A) - 1 != 0:
            count += 1

    for i in range(1, len(A) - 1):
        if A[i][0] % 2 == 0:
            count += 1
        if A[i][len(A[i]) - 1] % 2 == 0 and len(A[i]) - 1 != 0:
            count += 1
    return count


matrix = myfuntions.myInputMatrix()
print(solution(matrix))
