# /*
#    Viết chương trình đếm số hoàn thiện có trong một mảng các số nguyên có
#    n phần tử
# */
import myfuntions


def solution(n, lst):
    count = 0
    for i in range(0, n):
        if myfuntions.checkPerfectNumber(lst[i]):
            count += 1
    return count


n = int(input())
lst = myfuntions.myInput(n)
print(solution(n, lst))
