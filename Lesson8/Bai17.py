# /*
#     Cho 2 mảng A,B mỗi mãng có n phần tử. Thực hiện việc trộn xen kẽ
#     1 phần tử mảng A tới phần tử mảng B để tạo ra mảng C
# */
import myfuntions


def solution(lstA, lstB):
    lstC = []
    for i in range(0, len(lstA)):
        lstC.append(lstA[i])
        lstC.append(lstB[i])
    return lstC


n = int(input("Nhập vào số lượng phần tử cho mảng A: "))
lstA = myfuntions.myInput(n)
lstB = myfuntions.myInput(n)
print(solution(lstA,lstB))