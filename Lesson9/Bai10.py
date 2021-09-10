# // Cho 2 mảng a,b. Liệt kê các giá trị chỉ xuất hiện 1 trong 2 mảng
import myfuntions


def solution(A,B,C):
    for i in range(0,len(A)):
        if A[i] not in B:
            C.append(A[i])

n = int(input("Nhập số lượng phần tử cho mảng A"))
A = myfuntions.myInput(n)
m = int(input("Nhập số lượng phần tử cho mảng B"))
B = myfuntions.myInput(m)
C=[]
solution(A,B,C)
solution(B,A,C)
print(C)