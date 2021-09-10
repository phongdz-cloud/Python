# /*
#    Cho mảng một chiều các số thực hãy tìm đoạn [a,b] sao cho
#    đoạn này chứa tất cả các giá trị trong mảng.
# */
import myfuntions


def checkValid(n, x, y):
    if x >= n or x >= y:
        return False
    return True


def solution(n, lst, arr, x, y):
    if checkValid(n, x, y):
        i = x
        while i < n:
            arr.append(lst[i])
            i += 1
            if i > y:
                break
        return True
    return False


n = int(input())
lst = myfuntions.myInput(n)
x = int(input())
y = int(input())
arr = []
flag = solution(n, lst, arr, x, y)
print(arr if flag else "Input invalid")
