# /*
#     Kiểm tra dòng thứ k có giảm dần hay không?
# */
import myfuntions


def checkValid(k, A):
    return False if k < 0 or len(A[0]) < 0 or len(A) < 0 or k >= len(A) else True


def checkRowMatrix(A, k):
    for i in range(0, len(A[0]) - 1):
        if A[k][i] < A[k][i + 1]:
            return False
    return True


def solution(A, k):
    if checkValid(k, A):
        return "Dòng có thứ tự giảm dần" if checkRowMatrix(A, k) else "Dòng không có thứ tự giảm dần"


matrix = myfuntions.myInputMatrix()
k = int(input())
print(solution(matrix, k))
