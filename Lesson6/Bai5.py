# /*
#     Viết chương trình tính tổng các số chẵn trong một mảng các số nguyên không âm
# */
import myfuntions


def solution(n, A):
    sum = 0
    for i in range(0, n):
        if A[i] % 2 == 0 and A[i] > 0:
            sum += A[i]
    return sum


n = int(input())
A = myfuntions.myInput(n)
print(solution(n, A))
