marks=int(input("enter marks of a student:"))
print("the marks of student are:",marks)
if marks>80 and marks<100:
    print("grade A")
elif marks>70 and marks<80:
    print("grade B")
elif marks>55 and marks<70:
    print("grade C")
elif marks>30 and marks<55:
    print("grade D")
else:
    print("fail")
