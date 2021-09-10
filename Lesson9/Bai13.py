# // Hãy xóa tất cả các số chính phương trong mảng 1 chiều các số nguyên
import myfuntions


def solution(A):
    i = 0
    while i < len(A):
        if myfuntions.checkSquareNumber(A[i]):
            A.remove(A[i])
            i -= 1
        i+=1


n = int(input())
A = myfuntions.myInput(n)
solution(A)
print(A)
