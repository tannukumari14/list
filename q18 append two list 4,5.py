a= [1,2,3,4,5,6]
b= [2,3,1,0,6,7]
c=[]
i=0
while i<len(a):
    n=a[i]
    if n not in b:
        c.append(n)
    i=i+1
print(c)