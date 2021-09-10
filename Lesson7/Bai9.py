# /*
#    Tìm vị trí số nhỏ nhất trong một mảng số nguyên
# */
import myfuntions


def findMinArray(n, lst):
    min = lst[0]
    index = 0
    for i in range(0, n):
        if lst[i] < min:
            min = lst[i]
            index = i
    return index


n = int(input())
lst = myfuntions.myInput(n)
print(findMinArray(n, lst))
