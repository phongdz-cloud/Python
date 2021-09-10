# // Hãy đưa các số chẵn trong mảng về đầu mảng, các số lẻ về cuối mảng
# // và các phần tử 0 nằm giữa
import myfuntions


def checkEvenArray(A, index):
    k = -1
    for i in range(index + 1, len(A)):
        if A[i] % 2 == 0 and A[i] != 0:
            return i
        if A[i] == 0:
            k = i
    return k


def solution(A):
    for i in range(0, len(A)):
        if A[i] % 2 != 0 or A[i] == 0:
            index = checkEvenArray(A, i)
            if index != -1:
                myfuntions.mySwap(A, i, index)


n = int(input())
A = myfuntions.myInput(n)
solution(A)
print(A)
