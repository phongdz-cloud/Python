# /*
#     Cho số nguyên n nhập từ bàn phím. Viết chương trình đổi số này sang
#     các hệ nhị phân, bát phân, và thập lục phân. In kết quả ra màn hình
# */
import math

import myfuntions


def convertToBinary(n):
    s = ""
    while n != 0:
        s += chr((n % 2) + 48)
        n = math.floor(n / 2)

    return myfuntions.myReverse(s)


def convertToOctal(n):
    s = ""
    while n > 7:
        balance = n / 8
        s += chr(int((balance - math.floor(balance)) * 8 + 48))
        n = math.floor(n / 8)
    s += chr(n + 48)
    return myfuntions.myReverse(s)


def convertToHex(n, hex):
    s = ""
    while (n > 15):
        balance = n / 16
        index = int((balance - math.floor(balance)) * 16)
        s += hex[index]
        n = math.floor(n / 16)
    s += hex[n]
    return myfuntions.myReverse(s)


hex = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
];
n = int(input())
# print(convertToBinary(n)
# print(convertToOctal(n))
print(convertToHex(n,hex))
