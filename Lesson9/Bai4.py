# /*
#   Hãy liệt kê các giá trị trong mảng thỏa điều kiện
#   lớn hơn giá trị tuyệt đối của giá trị đứng liền sau nó
# */
import math

import myfuntions


def checkValue(a,b):
    return True if a >b else False

def solution(lst):
    lstB = []
    for i in range(0,len(lst)-1):
        if checkValue(math.fabs(lst[i]),math.fabs(lst[i+1])):
            lstB.append(lst[i])
    return lstB

n = int(input())
lst = myfuntions.myInput(n)
print(solution(lst))