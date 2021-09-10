# // Hãy xóa tất cả các phần tử trùng nhau trong mảng và chỉ giữ lại duy nhất một phần tử
import myfuntions


def checkMatch(A, x):
    count = 0
    for i in range(0, len(A)):
        if x == A[i]:
            count += 1
    return True if count == 1 else False


def solution(A):
    i = 0
    while i < len(A):
        if not checkMatch(A, A[i]):
            A.remove(A[i])
        else:
            i += 1


n = int(input())
A = myfuntions.myInput(n)
solution(A)
print(A)
