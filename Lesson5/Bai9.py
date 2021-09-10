# //Nhập vào 4 số nguyên a, b, c, d. Tính a/b + c/d. Yêu cầu xuất ra dạng phân số tối giản.
import myfuntions


def solution(a, b, c, d):
    if b == 0 or d == 0:
        return False
    param.numerator = a * d + c * b
    param.demoninator = b * d
    gcf = myfuntions.gcd(param.numerator, param.demoninator)
    param.numerator /= gcf
    param.demoninator /= gcf
    return True


a = int(input())
b = int(input())
c = int(input())
d = int(input())
param = myfuntions.param(0, 0)
print("{0} / {1}".format(param.numerator, param.demoninator) if solution(a, b, c, d) else "Không chia được")
