# a=[[2,3],[4,5,3,5],[5],[4,5,6,7,8,9]]
# i=0
# while i<len(a):
#     j=0
#     while len(a[j])<len(a[i]):
#         j=j+1
#     i=i+1
# print("max len",len(a[j]),a[j])

# a=[[2,3],[4,5,3,5],[4,5,6,7,8,9],[1,2,7]]
# i=0
# d=[]
# p=a[0]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i]>d:
#             d=a[i]
#         if a[i]<p:
#             p=a[i]
#         j=j+1
#     i=i+1
# print("max len",d)
# print("min len",p)

a=input("enter the name")
i=0
vowel=0
consonant=0
while i<len(a):
    if a[i]=="a" or a[i]=="i" or a[i]=="o" or a[i]=="e" or a[i]=="u":
        vowel=vowel+1
    else:
        consonant=consonant+1
    i=i+1
print("vowel",vowel)
print("consonant",consonant)