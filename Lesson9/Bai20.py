# /*
#     Cho mảng A có nA phần tử và mảng B có nB phần tử. Tạo mảng C xen kẽ 1 phần tử mảng A
#     tới phần tử mảng B. các phần tử dư ra (không còn xen kẽ được nữa) thì nối hết vào đuôi
#     mảng C
# */
import myfuntions


def solution(A, B):
    C = []
    i = j = 0
    while i < len(A) and j < len(B):
        C.append(A[i])
        C.append(B[j])
        i += 1
        j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C


n = int(input("Nhập số lượng phần tử của A: "))
A = myfuntions.myInput(n)
m = int(input("Nhập số lượng phần tử của A: "))
B = myfuntions.myInput(m)
print(solution(A, B))
