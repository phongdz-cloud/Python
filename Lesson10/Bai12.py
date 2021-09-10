# /*
#     Tính tổng trên các dòng, các cột, trên đường chéo chính, đường chéo phụ
# */
import math

import myfuntions


def solution(A):
    sum = 0
    for i in range(0, len(A)):
        sum += A[i][i] + A[i][len(A[i]) - i - 1]
    if len(A[0]) % 2 != 0:
        sum -= A[math.floor(len(A[0]) / 2)][math.floor(len(A[0]) / 2)]
    return sum


matrix = myfuntions.myInputMatrix()
print(solution(matrix))
