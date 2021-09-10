# /*
#    Viết chương trình đảo ngược mảng ban đầu
# */
import myfuntions


def reverseArray(n, lst):
    i = 0
    j = n - 1
    while j > i:
        myfuntions.mySwap(lst, i, j)
        i += 1
        j -= 1
    return lst


n = int(input())
lst = myfuntions.myInput(n)
print(reverseArray(n, lst))
