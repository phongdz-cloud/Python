# //Nhập một chữ cái. Nếu là chữ thường thì đổi sang chữ hoa, ngược lại đổi sang chữ thường.
def solution(c):
    c = str(c)
    return (c.upper() if (c >= "a" and c <= "z") else c.lower())

c = input()[0]
print(solution(c))