# /*
#     Tìm vị trí (tọa độ dòng, cột) của số nguyên tố đầu tiên trong mảng 2 chiều m dòng
#     , n cột
# */
import myfuntions


def solution(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            if myfuntions.checkPrimeNumber(A[i][j]):
                print("{0} {1}".format(i, j))
                return


matrix = myfuntions.myInputMatrix()
solution(matrix)
