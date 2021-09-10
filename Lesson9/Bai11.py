# // Hãy cho biết tất cả phần tử trong mảng a có nằm trong mảng b hay không
import myfuntions


def solution(A,B):
    count =0
    for i in range(0,len(A)):
        if A[i] in B:
            count+=1
    return count == len(A)

n = int(input("Nhập số lượng phần tử cho mảng A"))
A = myfuntions.myInput(n)
m = int(input("Nhập số lượng phần tử cho mảng B"))
B = myfuntions.myInput(m)
print(solution(A,B))