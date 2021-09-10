# /*
#     Viết chương trình tính tổng các phần tử trong một mảng 2 chiều có kích thước MxN
# */
import myfuntions


def solution(matrix):
    sum = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sum += matrix[i][j]
    return sum


matrix = myfuntions.myInputMatrix()
print(solution(matrix))
