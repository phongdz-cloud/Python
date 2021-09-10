# //Nhập vào 3 số thực. Cho biết 3 số vừa nhập có phải là độ dài cạnh của 1 tam giác nào đó hay không, nếu phải thì
# // thì cho biết đó là loại tam giác gì? (Đều, vuông cân, vuông, cân, thường)i
import myfuntions as f


def solution(a, b, c, flag):
    if not flag:
        print("Ba cạnh vừa nhập không tạo thành một tam giác")
    else:
        if a == b and b == c:
            print("Tam giác đều")
        elif (
                b * b + c * c - a * a < 0.0001 or
                a * a + c * c - b * b < 0.0001 or
                a * a + b * b - c * c < 0.0001
        ):
            if a != b and a != c and b != c:
                print("Tam giác vuông")
            else:
                print("Tam giác vuông cân")
        elif a == b or a == c or b == c:
            print("Tam giác cân")
        else:
            print("Tam giác thường")


a = float(input())
b = float(input())
c = float(input())
flag = f.checkTriangle(a, b, c)
solution(a, b, c, flag)
