# /*
#     Viết chương trình tính tổng hai ma trận
# */
import myfuntions

def solution(matrixA,matrixB):
    matrixC = []
    for i in range(0,len(matrixA)):
        column = []
        for j in range(0,len(matrixA[i])):
            column.append(matrixA[i][j] + matrixB[i][j])
        matrixC.append(column)
    return matrixC

matrixA= myfuntions.myInputMatrix()
matrixB= myfuntions.myInputMatrix()
print(solution(matrixA,matrixB))
