# /* Có một máy ATM với số lượng tiền có trong máy là vô hạn. Máy có bốn loại tiền là
# 100.000VNĐ, 50.000VNĐ, 20.000VNĐ và 10.000VNĐ
# Một khách hàng cần rút số tiền là n (n chia hết cho 10.000), hãy tìm ra phương án đưa tiền cho khách
# hàng sao cho số tờ tiền là ít nhất. Gỉa sử số lượng các tờ tiền của mỗi loại tiền là vô hạn
# */
def checkValid(n):
    if n % 10000 == 0:
        return True
    return False


def solution(n, flag):
    if flag:
        count = 0
        while n > 0:
            if n >= 100000:
                n -= 100000
            elif n >= 50000:
                n -= 50000
            elif n >= 20000:
                n -= 20000
            elif n >= 10000:
                n -= 10000
            count += 1
        return count
    return -1


n = int(input())
flag = checkValid(n)
result = solution(n, flag)
print(result if flag else "Không tính được")
