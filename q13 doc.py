# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist) 

# a=["tanu","nisha"]
# b=[1,2,3,4,a]
# print(b)

# a=[4,5,[6,7],8,9,[12,13]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         j=input("enter the number")
# i=0
# while i<len(j):
#     print(int(j[i])*int(j[i]))
#     i=i+1
# print()
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)

# x=int(input("enter the number"))
# y=x**0.5
# z=int(y)
# print(z)


# n=["tanu","nisha","sneha","jiya","neha","sneha"]
# n[0]="abhishek"
# print(n)


# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.insert(0,"abhishek")
# print(names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# print(names_list)
# names_list.append("dhruv")
# print(len(names_list))
# print(names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.append("alok")
# print("length of the list is ", len(names_list))
# print(names_list)

# a=["tanu","khushboo","shivani","razia","simran"]
# a.pop()
# print(a)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# names_list.pop()
# print("length of the list is ", len(names_list))
# print(names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("length of the list is ", len(names_list), names_list)
# names_list.pop(2)
# print("length of the list is ", len(names_list), names_list)
# names_list.pop(2)
# print("length of the list is ", len(names_list), names_list)


# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("shivam" in names_list)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# if "shivam" in names_list:
#     print("Shivam ka naam names_list mei hai")
# else:
#     print("Shivam ka naam names_list mei nahi hai.")


# a=["tanu","kumari","pinky","mandal","kaamini","verma"]
# b=len(a)
# i=0
# while i<b:
#     print(a[i])
#     i=i+1

# a=[23,45,89,90,56,80]
# l=len(a)
# i=0
# m=0
# while i<len(a):
#     m=m+a[i]
#     i=i+1
# print(m)


# a=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
# l=len(a)
# i=0
# less_than50=0
# more_than50=0
# while i<l:
#     m=a[i]
#     if m<50:
#         less_than50=less_than50+1
#     else:
#         more_than50=more_than50+1
#     i=i+1
# print(more_than50)
# print(less_than50)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(len(numbers))

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(count.numbers)

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(max(numbers))

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# a=0
# i=0
# while i<len(numbers):
#     if numbers[i]>a:
#         a=numbers[i]
#     i=i+1
# i=0
# b=0
# while i<len(numbers):
#     if numbers[i]>b:
#         if numbers[i]!=a:
#             b=numbers[i]
#     i=i+1
# print(b)


# a=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# a.reverse()
# print(a)


# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# while i<len(numbers):
#     count=count+1
#     print(count)
#     i=i+1

# numbers=[50,40,23,70,56,12,5,10,7,34]
# i=0
# count=0
# while i<len(numbers):
#     if numbers[i]>20 and numbers[i]<40:
#         count=count+1
#         print(numbers[i],count)
#     i=i+1

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=1
# a=1
# while i<len(numbers):
#     if numbers[i]>a:
#         a=numbers[i]
#     i=i+1
# print(a)


# a=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# b=[]
# while i<len(a):
#     a.reverse()
#     i=i+1
# print(a)


# a=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(a):
#     i=i+1
# print(a)

# a="tanu,sneha,neha,jiya,nisha"
# b=a.split(",")
# print(b)

# a="tanu"
# b=list(a)
# print(b)

# a=["tanu","khushboo","seerat khushboo ki biwi"]
# b=[1,2,3,3]
# a.extend(b)
# print(a)

# a=["tanu","nisha","tanushree"]
# i=2
# c="ishu"
# while i<len(a):
#     a.insert(i,c)
#     i+=i+1
# print(a)

# a=["tanu","shree","anuu"]
# a.insert(2,"owl")
# print(a)

# a=[1,5,78,90,54]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     b=sum/(a[i])
#     i=i+1
# print(sum,b)


