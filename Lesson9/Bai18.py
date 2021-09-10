# //Hãy "dịch phải xoay vòng" k lần phần tử trong mảng
import myfuntions


def solution(A, k):
    while (k > 0):
        x = A[len(A) - 1]
        A.pop()
        A.insert(0, x)
        k -= 1


n = int(input())
A = myfuntions.myInput(n)
k = int(input())
solution(A, k)
print(A)
