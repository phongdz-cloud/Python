# /*
#   Cho mảng 1 chiều các số thực. Hãy viết hàm liệt kê tất cả các giá trị trong mảng
#   có ít nhất 1 lân cận trái dấu nó
# */
import myfuntions


def checkValid(a,b):
    return a * b < 0
def solution(lstA):
    lstB =[]
    if len(lstA) > 1:
        if checkValid(lstA[0],lstA[1]):
            lstB.append(lstA[0])
        for i in range(1,len(lstA)-1):
            if checkValid(lstA[i],lstA[i-1]) or checkValid(lstA[i], lstA[i + 1]):
                lstB.append(lstA[i])
        if checkValid(lstA[len(lstA)-1], lstA[len(lstA)-2]):
            lstB.append(lstA[len(lstA)-1])
    return lstB

n = int(input())
lstA = myfuntions.myInput(n)
print(solution(lstA))