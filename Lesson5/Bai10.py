# //Tìm và in lên màn hình tất cả các số nguyên trong phạm vi từ 10 tới 99 sao cho tích cửa 2 chữ số
# //bằng 2 lần tổng của 2 chữ số đó
import math


def calculate(i):
    temp = i
    a = temp % 10
    temp = math.floor(temp / 10)
    b = temp % 10
    temp = math.floor(temp / 10)
    if a * b == 2 * (a + b):
        return True
    return False


def solution():
    lst = []
    for i in range(1, 100):
        if calculate(i):
            lst.append(i)
    return lst


print(solution())
