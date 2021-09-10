# /*
#     Viết chương trình đếm các số âm trong một mảng các số nguyên
# */
import myfuntions


def solution(n, A):
    count = 0;
    for i in range(0, n):
        if (A[i] < 0):
            count += 1
    return count


n = int(input())
A = myfuntions.myInput(n)
print(solution(n, A))
