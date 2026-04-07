num=int(input("enter a number:"))
i = 0
while i<num:
    i += 1
    if i%2 == 0:
        continue
    if i==7:
        break
    if num<0:
        pass
    print(i)
