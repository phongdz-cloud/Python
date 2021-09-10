# //Kiểm tra xem n vừa nhập có phải gồm toàn các chữ số chẵn không?
import math
def findEvenNumber(n):
    while n > 0:
        if n % 2 !=0:
            return False
        n = math.floor(n/10)
    return True

n = int(input())
print("N toàn chữ số chẵn" if findEvenNumber(n) else "N không toàn chữ số chẵn")
