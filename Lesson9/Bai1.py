# /*
#     Cho mảng số nguyên A. Tạo ra 2 mảng B va C theo quy tắc: mảng B gồm
#     các phần tử dương hoặc bằng 0 của A và mảng C gồm các phần tử âm của A
# */
import myfuntions


def checkValid(n):
    return True if n >= 0 else False


def solution(lstA, lstB, lstC):
    for i in range(0, len(lstA)):
        if checkValid(lstA[i]):
            lstB.append(lstA[i])
        else:
            lstC.append(lstA[i])


n = int(input())
lstA = myfuntions.myInput(n)
lstB = []
lstC = []
solution(lstA, lstB, lstC)
print(lstB)
print(lstC)
