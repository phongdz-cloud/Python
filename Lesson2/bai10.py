# /*
# Nhập vào giờ, phút, giây. Cho biết một giây sau đó là mấy giờ, mấy phút, mấy giây
# */
def checkTime(h, m, s):
    if h >= 0 and s >= 0 and m >= 0:
        if h < 24 and m < 60 and s < 60:
            return True
    return False


def solution(h, m, s, flag):
    if flag:
        if s == 59:
            s = 0
            if m == 59:
                m = 0
                if h == 23:
                    h = 0
                else:
                    h += 1
            else:
                m += 1
        else:
            s += 1
    output(h, m, s, flag)


def output(h, m, s, flag):
    print("{0} giờ {1} phút {2} giây".format(h, m, s) if flag else "Gio phút giây không hợp lệ")


h = int(input())
m = int(input())
s = int(input())
flag = checkTime(h, m, s)
solution(h, m, s, flag)
