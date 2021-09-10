# //Nhập 3 số nguyên a,b,c đôi một khác nhau. Tìm số có giá trị nhỏ nhì
def findMax(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max


def solution(a, b, c):
    secondNumber = a
    maxNumber = findMax(a, b, c)
    if (secondNumber < b != maxNumber) or (maxNumber == secondNumber > b):
        secondNumber = b
    if (secondNumber < c != maxNumber) or (c < secondNumber == maxNumber):
        secondNumber = c
    return secondNumber


a = int(input())
b = int(input())
c = int(input())
print("Số có giá trị lớn nhì là: {0}".format(solution(a, b, c)))
