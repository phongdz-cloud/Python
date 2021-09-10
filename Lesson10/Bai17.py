# /*
#     Đếm số lượng giá trị "hoàng hậu" trên ma trận. Một phần tử gọi là hoàng hậu khi nó
#     lớn nhất trên dòng, cột và 2 đường chéo
# */
import myfuntions


def checkRowMatrix(A, x, row):
    for i in range(0, len(A[row])):
        if A[row][i] > x:
            return False
    return True


def checkColumnMatrix(A, x, column):
    for i in range(0, len(A)):
        if A[i][column] > x:
            return False
    return True


def checkDiagonalLine(A, i, j, x):
    k = 0
    while k < len(A):
        if i - k - 1 >= 0 and j - k - 1 >= 0 and A[i - k - 1][j - k - 1] > x:
            return False
        if i + k + 1 < len(A) - 1 and j + k + 1 <= len(A[i]) - 1 and A[i + k + 1][j + k + 1] > x:
            return False
        k += 1
    return True


def queueNumber(A):
    count = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if checkRowMatrix(A, A[i][j], i) and checkColumnMatrix(A, A[i][j], j) and checkDiagonalLine(A, i, j,
                                                                                                        A[i][j]):
                count += 1
    return count


matrix = myfuntions.myInputMatrix()
print(queueNumber(matrix))
