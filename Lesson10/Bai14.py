# /*
#     Tìm và in ra tất cả vị trí xuất hiện của số lớn nhất trong ma trận.
# */
import myfuntions


def findMaxMatrix(A):
    max = A[0][0]
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if A[i][j] > max:
                max = A[i][j]
    return max


def solution(A):
    max = findMaxMatrix(A)
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if A[i][j] == max:
                print("{0} {1}".format(i, j))


matrix = myfuntions.myInputMatrix()
solution(matrix)