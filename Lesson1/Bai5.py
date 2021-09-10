# Nhập vào một năm. Cho biết năm đó có phải năm nhuận hay không
def checkLeapYear(year):
    if(year % 400 == 0):
        return True
    if(year % 4 == 0 & year % 100 !=0):
        return False
    return False



a = int(input())
print(checkLeapYear(a))
