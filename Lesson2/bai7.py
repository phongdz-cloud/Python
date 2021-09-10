# //Nhập vào số nguyên a,b,c. Tìm nghiệm phương trình ax^2 + bx +c =0
import math


def solution(a, b, c):
    flag = 1
    if a == 0 and b == 0 and c == 0:
        flag = -1
    delta = b * b - 4 * a * c
    if delta < 0:
        flag = 0
    else:
        if delta > 0:
            delta = math.sqrt(delta)
            x1 = (-b * 1.0 + delta) / (2 * a)
            x2 = (-b * 1.0 - delta) / (2 * a)
            flag = 2
        else:
            x1 = (b * 1.0) / (2 * a)
    output(x1, x2, flag)


def output(x1, x2, flag):
    if flag == -1:
        print("Phương trình vô số nghiệm")
    elif flag == 0:
        print("Phương trình vô nghiệm")
    elif flag == 1:
        print("Phương trình có nghiệm kép x = {0}".format(x1))
    else:
        print("Phương trình có 2 nghiệm phân biệt x1 = {0} và x2 = {1}".format(x1,x2))


a = int(input())
b = int(input())
c = int(input())
solution(a, b, c)
