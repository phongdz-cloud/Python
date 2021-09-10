# /*
#   Tính tổng các phần tử "cực trị" trong mảng. Một phần tử được gọi là cực trị
#   khi nó lớn hơn hoặc nhỏ hơn các phần tử xung quanh nó
# */
import myfuntions


def checkValid(a,b):
    return a > b or a < b
def solution(A):
    sum = 0
    if len(A) > 1:
        if checkValid(A[0],A[1]):
            sum+=A[0]
        for i in range(1,len(A)-1):
            if checkValid(A[i],A[i-1]) or checkValid(A[i],A[i+1]):
                sum +=A[i]
        if checkValid(A[len(A)-1],A[len(A)-2]):
            sum+=A[len(A)-1]
    return sum

n = int(input())
A = myfuntions.myInput(n)
print(solution(A))