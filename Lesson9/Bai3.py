# /*
#    Viết chương trình nhập vào một dãy số A gồm m số thực, nhập vào dãy số B gồm
#      n số thực. In ra những phần tử xuất hiện ở cả 2 dãy
# */
import myfuntions


def solution(lstA, lstB):
    lstC = []
    for i in range(0, len(lstA)):
        if lstA[i] in lstB:
            lstC.append(lstA[i])
    return lstC

n = int(input("Nhập vào số lượng phân tử A: "))
lstA = myfuntions.myInputFloat(n)
m = int(input("Nhập vào số lượng phân tử B: "))
lstB = myfuntions.myInputFloat(m)
print(solution(lstA, lstB))