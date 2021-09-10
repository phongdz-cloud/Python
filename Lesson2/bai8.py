# /*
# Nhập một số bất kỳ. Hãy viết bằng chữ giá trị của số nguyên đó nếu có giá trị từ 0 đến 9, ngược lại thông báo
# không biết viết
# */
def output(numbers, number):
    print(numbers[number] if 0 <= number <= 9 else "Không biết viết")


numbers = ["Không",
           "Một",
           "Hai",
           "Ba",
           "Bốn",
           "Năm",
           "Sáu",
           "Bảy",
           "Tám",
           "Chín"]
number = int(input())
output(numbers, number)
