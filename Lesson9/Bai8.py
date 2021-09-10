# // Liệt kê tần suất xuất hiện các giá trị trong mảng (Lưu ý: mỗi giá trị liệt kê 1 lần)
import myfuntions


def solution(A, B, C):
    for i in range(0, len(A)):
        if A[i] not in B:
            count = 0
            for j in range(0, len(A)):
                if A[i] == A[j]:
                    count += 1
            B.append(A[i])
            C.append(count)


n = int(input())
A = myfuntions.myInput(n)
B = []
C = []
solution(A, B, C)
print(B)
print(C)
