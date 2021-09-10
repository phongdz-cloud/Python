# /*
#     Đếm số lượng giá trị "yên ngựa" trên ma trận. Một phần tử gọi là "yên ngựa"
#     khi nó lớn nhất trên dòng và nhỏ nhất trên cột
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


def horseSaddle(A):
    count = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if checkRowMatrix(A, A[i][j], i) and checkColumnMatrix(A, A[i][j], j):
                count += 1
    return count


matrix = myfuntions.myInputMatrix()
print(horseSaddle(matrix))
