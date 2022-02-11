a=int(input("enter the number"))
b=int(input("enter the number"))
sign=(input("enter the sign"))
i=0
while i<a:
    if sign=="+" :
        print(a+b)
    elif sign=="-" :
        print(a-b)
    elif sign=="*" :
        print(a*b)
    elif sign=="**": 
        print(a*b)
    elif sign=="/":
        print(a/b)
    elif sign=="//":
        print(a//b)
    elif sign=="%":
        print(a%b)
    else:
        print("no")
    i=i+1