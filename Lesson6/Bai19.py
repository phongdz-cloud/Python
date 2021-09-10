# /*
#    Hay liệt kê các số trong mảng 1 chiều các số thực thuộc đoạn [x,y] cho trước
# */
import myfuntions


def checkValid(n, lst, x, y):
    if x >= n or x >= y:
        return False
    return True


def solution(n, lst, arr, x, y):
    if checkValid(n, lst, x, y):
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
arr = []
x = int(input())
y = int(input())
flag = solution(n, lst, arr, x, y)
print(arr if flag else "Đầu vào không hợp lệ")
