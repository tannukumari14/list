a=[]
i=0
while i<5:
    num=int(input("enter the number"))
    a.append(num)
    i=i+1
print(a)

i=0
b=[]
while i<10:
      user=int(input("enter the number"))
      b.append(user)
      i+=1
j=1
x=[]
while j<len(b)+1:
      x.append(b[-j])
      j+=1
print(x)
sum=1
y=0
while y<len(x):
      sum=sum*x[y]
      y+=1
print(sum)

