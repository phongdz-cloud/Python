# //Kiểm tra các chữ số n có tăng dần hay không
import math


def findAscendingNumber(n):
    temp = n % 10
    while n > 0:
        n = math.floor(n / 10)
        if temp <= n % 10:
            return False
        temp = n % 10
    return True


n = int(input())
print("Các chữ số tăng dần" if findAscendingNumber(n) else "Các chữ số không tăng dần")
