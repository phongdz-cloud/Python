# // Nhập 4 số thực a,b,c,d. Tìm số có giá trị lớn nhất

def solution(a, b, c, d):
    max = a
    if (max < b):
        max = b
    if (max < c):
        max = c
    if (max < d):
        max = d
    return max

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(solution(a,b,c,d))
