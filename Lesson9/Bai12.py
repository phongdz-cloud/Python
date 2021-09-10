# // Hãy xóa tất cả các số lớn nhất trong mảng các số thực
import myfuntions


def findMaxArray(A):
    max = A[0]
    for i in range(0, len(A)):
        if A[i] > max:
            max = A[i]
    return max


def solution(A):
    max = findMaxArray(A)
    while max in A:
        A.remove(max)

n = int(input())
A = myfuntions.myInput(n)
solution(A)
print(A)
