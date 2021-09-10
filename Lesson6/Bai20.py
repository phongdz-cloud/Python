# /*
#    Hãy liệt kê các số chẵn trong mảng 1 chiều các số nguyên thuộc đoạn [x,y] cho truóc
#    (x,y là các số nguyên)
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
            if lst[i] % 2 == 0:
                arr.append(lst[i])
            if i > y:
                break
            i += 1
        return True
    return False


n = int(input())
lst = myfuntions.myInput(n)
arr = []
x = int(input())
y = int(input())
flag = solution(n, lst, arr, x, y)
print(arr if flag else "Đầu vào không hợp lệ")
