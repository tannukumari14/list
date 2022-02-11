a=[2,3,4,5,6]
max=0
i=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    i=i+1
print("first maximum",max) 
max1=0
i=0
while i<len(a):
    if max1<a[i]:
        if a[i]!=max:
            max2=a[i]  
        i=i+1
print("second maximum ",max2)             
