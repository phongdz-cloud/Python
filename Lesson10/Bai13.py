# /*
#     Sắp xếp ma trận sao cho các phần tử trên đường chéo chính tăng dần
# */
import myfuntions


def solution(A):
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[i][i] > A[j][j]:
                temp = A[i][i]
                A[i][i] = A[j][j]
                A[j][j] = temp
    return A


matrix = myfuntions.myInputMatrix()
print(solution(matrix))
