# a=[1,5,7,8,9]
# b=[6,5,8,4,0]
# i=0
# c=[]
# while i<len(a):
#     if a[i]==b[i]:
#         c=a[i] not in b[i]
#         c.append(str(a[i]),str(b[i]))
#         i=i+1
# print(c)

# a=[1,2,3,4,6,7]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     while i>j:
#         if a[i]+a[j]:
#             c.append([str(a[i])+str(a[j])])
#         j=j+1
#     i=i+1
# print(c)

# a=[5,4,3,8,9]
# s=[4,5,8,9,0]
# i=0
# b=[]
# while i<len(a):
#     n=a[i]
#     if n not in b:
#         b.append(n)
#         i=i+1
# print(b)

# a_list=["a","b","c"]
# index1=a_list.index("a")
# index2=a_list.index("b")
# a_list[index1],a_list[index2]=a_list[index2],a_list[index1]
# print(a_list)

# a=[0,1,2,3,4,5]
# index1=a.index(0)
# index2=a.index(1)
# index3=a.index(2)
# index4=a.index(3)
# index5=a.index(4)
# index6=a.index(5)
# a[index1],a[index2]=a[index2],a[index1]
# a[index3],a[index4]=a[index4],a[index3]
# a[index5],a[index6]=a[index6],a[index5]
# print(a)

# a=[1,2,3,4]
# a+=[a.pop(0)]
# print(a)

# a=[1,2,3,4]
# i=0
# k=[]
# while i<len(a):
#     k.append(a[-i])
#     i=i+1
# print(k)

# a=[3,5,8,9,0]
# print(a[0])

# a=[5,4,2,8,9,0]
# b=[1,2,6,7,8,9]
# c=a+b
# i=0
# while i<len(a):
#     i=i+1
# print(c)

# a=[1,2,3]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while 

# a=12435
# print(a%10)


# i=5
# while i>=0:
#     b=5-i
#     while b>0:
#         print(" ",end=" ")
#         b=b-1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i-1

# a=[1,2,3,34,5,16,7,8]
# i=1
# b=[]
# x=0
# while i<len(a):
#     c=a[i]-a[x]
#     b.append(c)
#     i=i+1
#     x=x+1
# print(b)

# a=7.9+8.9+1j
# print(a)


# a=[1,7,9,5,3,2,12,1,3,5]
# c=[8,9,0,1,4,7,5,6,2,1,2]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<a:
#         b.append(c)
#         j=j+1
#     i=i+1
# print(b)


# for i in range(2,11,2):
# print(i)

# a=[10,20,30]
# c=[40,50,60]
# c.extend(a)
# print(c)

# i=0
# num=int(input("enter the number"))
# while i<1:
#     if num>8:
#         print(num,"greater")
#     i=i+1

# a=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
# i=0
# b=[]
# while i<len(a):
#     h=a[i]
#     if h not in b:
#         b.append(h)
#     i=i+1
# print(b)


# a=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
# i=0
# while i<len(a):
#     j=i+1
#     while j<len(a):
#         if a[i]==a[j]:
#             del(a[j])
#             j=j+1
#         i=i+1
# print(a)

# a=["tanu"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     x=10
#     while j<len(a[i]):
#         b.append(a[i][j])
#         b.append(x)
#         x=x+10
#         j=j+1
#     i=i+1
# print(b)

a="tanu"
i=0
j=10
b=[]
while i<len(a):
    if a[i] not in b:
        c=a[i]
        b.append(c)
        b.append(j)   
    j=j+10
    i=i+3
print(b)