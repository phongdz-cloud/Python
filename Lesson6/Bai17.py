# /*
#    Viết chương trình tìm số lớn nhất trong một mảng số nguyên
# */
import myfuntions


def findMaxArray(n, lst):
    max = lst[0]
    for i in range(0, n):
        if lst[i] > max:
            max = lst[i]
    return max


n = int(input())
lst = myfuntions.myInput(n)
print(findMaxArray(n, lst))
