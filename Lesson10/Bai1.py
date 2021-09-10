# /*
#     Viết chương trình nhập vào một số ở hệ 16, đổi số này sang hệ 10
# */
import math

import myfuntions


def checkValid(s):
    for i in range(0, len(s)):
        if (s[i] < 'A' or s[i] > 'F') and (s[i] < '0' or s[i] > '9'):
            return False
    return True


def checkHexDigit(s, hex):
    for i in range(0, 16):
        if s == hex[i]:
            decimal = i
            break
    return decimal


def reverse(s):
    return s[::-1]


def solution(s, hex):
    if checkValid(s):
        s = reverse(s)
        sum = k = 0
        for i in range(0, len(s)):
            convertToDecimal = checkHexDigit(s[i], hex)
            sum += convertToDecimal * math.pow(16, k)
            k += 1
        return sum
    return -1


hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
s = input()
print(solution(s, hex))
