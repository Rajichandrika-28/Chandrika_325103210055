x=int(input("enter x value"))
y=int(input("enter y value:"))
z=int(input("enter z value:"))
if x>y and x>z:
    print("x is greatest")
elif x<y and y>z:
    print("y is greatest")
else:
    print("z is greatest")
