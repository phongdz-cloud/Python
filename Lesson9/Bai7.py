# /*
#   Đếm số lượng giá trị lớn nhất có trong mảng 1 chiều các số thực
# */
import myfuntions


def findMaxArray(A):
    max = A[0]
    for i in range(0,len(A)):
        if A[i] > max:
            max = A[i]
    return max

def solution(A):
    max = findMaxArray(A)
    count =0
    for i in range(0,len(A)):
        if max == A[i]:
            count+=1
    return count

n = int(input())
A = myfuntions.myInputFloat(n)
print(solution(A))