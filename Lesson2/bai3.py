# //Nhập 3 số nguyên a,b,c. Tìm số có giá trị nhỏ nhất (min)
def solution(a,b,c):
    min = a
    if (min > b ):
        min = b
    if (min > c):
        min = c
    return min

a = int(input())
b = int(input())
c = int(input())
print(solution(a,b,c))