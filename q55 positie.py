a=[1,2,3,-0,-9,-6]
pos=0
neg=0
i=0
d=[]
e=[]
s=[]
while i<len(a):
    if a[i]>0:
        d.append(a[i])
        pos=pos+1
    elif a[i]<0:
        e.append(a[i])
        neg=neg+1
    i=i+1
print(d)
print(d[1])