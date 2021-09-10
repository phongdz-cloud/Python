import  myfuntions as f

a = float(input())
b = float(input())
c = float(input())
print("Ba cạnh đã cho lập thành một tam giác!" if f.checkTriangle(a,b,c) else
      "Ba cạnh đã cho không lập thành một tam giác!")

