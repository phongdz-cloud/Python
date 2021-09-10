# /*
#     Cho ma trận vuông A[20][20], có kích thước N. Viết chương trình sắp xếp lại
#     ma trận tăng dần theo dòng và cột
# */
import myfuntions


def matrixToArray(A):
    arr = []
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            arr.append(A[i][j])
    arr.sort()
    return arr


def solution(A):
    arr = matrixToArray(A)
    k = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            A[i][j] = arr[k]
            k += 1
    return A


matrix = myfuntions.myInputMatrix()
print(solution(matrix))
