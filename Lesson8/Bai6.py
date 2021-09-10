# /*
# Viết chương trình tìm và đổi chỗ phần tử lớn nhất và phần tử nhỏ nhất trong mảng
# */
import myfuntions


def solution(n, lst):
    indexMin = indexMax = 0
    min = max = lst[0]
    for i in range(0, n):
        if lst[i] < min:
            min = lst[i]
            indexMin = i
        if lst[i] > max:
            max = lst[i]
            indexMax = i
    myfuntions.mySwap(lst, indexMax, indexMin)


n = int(input())
lst = myfuntions.myInput(n)
solution(n, lst)
print(lst)
