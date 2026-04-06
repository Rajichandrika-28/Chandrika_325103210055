#arthematic operator
a=int(input("enter a number: "))
b=int(input("enter a number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
#assignment operators
print(a+=3)
print(b-=3)
print(a*=3)
print(b/=3)
print(a%=3)
print(b//=3)
print(a**=3)
ptint(b&=3)
print(b|=3)
#comparision operator
print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>b:",a>b)
print("a<b:",a<b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)
#logical operator
print(a>0 or b<0)
print(a<5 or b<10)
print(not(a<0 and b<10))
#identity operator
x=["python","program"]
y=["python","program"]
z=y
s=["apple","mango"]
t=["apple","banana"]
print(x==y)
print(x is not y)
print(y is z)
print(s==t)
print(s is t)
#membership operator
languages=["c","c++","python"]
subjects=["english","maths","pysics"]
print("c" not in languages)
print("python" in languages)
print("social in subjects")
#bitwise operator
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a>>1)
print(b<<1)
