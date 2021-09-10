# //Kiểm tra các chữ số n có giảm dần hay không
import math


def findDecreaseNumber(n):
    temp = n % 10
    while n > 0:
        n = math.floor(n / 10)
        if temp >= n != 0:
            return False
        temp = n % 10
    return True


n = int(input())
print("Các chữ số giảm dần" if findDecreaseNumber(n) else " Các chữ số không giảm dần")
