# /*
#     Viết chương trình tìm UCLN của một mảng n phần tử nguyên dương
# */
import math

import myfuntions


def solution(n, lst):
    if n > 1:
        u = myfuntions.gcd(math.fabs(lst[0]), math.fabs(lst[1]))
        for i in range(1, n - 1):
            u = myfuntions.gcd(u, math.fabs(lst[i + 1]))
        return u
    return 1


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
