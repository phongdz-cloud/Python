# Nhập 2 số nguyên a, b. Xuất ra số lớn nhất
def solution(a,b):
    if(a > b):
        return a
    elif(a<b):
        return b
    else:
        return a

a = int(input())
b = int(input())
print(solution(a,b))
