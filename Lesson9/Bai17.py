# //Hãy "dịch trái xoay vòng" các phần tử trong mảng
import myfuntions


def solution(A):
    x = A[0]
    del A[0]
    A.append(x)


n = int(input())
A = myfuntions.myInput(n)
solution(A)
print(A)
