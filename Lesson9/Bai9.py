# // Cho 2 mảng a,b. Đếm số lượng các giá trị chỉ xuất hiện 1 trong 2 mảng
import myfuntions


def solution(A,B):
    count =0
    for i in range(0,len(A)):
        if A[i] in B:
            count+=1
    return count

n = int(input("Nhập số lượng phần tử cho mảng A"))
A = myfuntions.myInput(n)
m = int(input("Nhập số lượng phần tử cho mảng B"))
B = myfuntions.myInput(m)
print(solution(A,B))

