# #7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# #Sample String : 'The quick Brow Fox'
# #Expected Output :
# #No. of Upper case characters : 4
# #No. of Lower case Characters : 11
# def calculate_latter(n):
#     count=0
#     COUNT=0
#     for i in range(len(n)):
#         if n[i]>='a' and n[i]<='z':
#             count=count+1
#         elif n[i]>='A' and n[i]<='Z':
#             COUNT+=1
#         else:
#             pass
#         i=i+1
#     print(COUNT)
#     print(count)
# calculate_latter('The Quick Brow Fox')



list1=[2,3,4,5,6,8,9,13,17]
list2=[]
i=len(list1)-1
while i>=0:
    list2.append(list1[i])
    i=i-2
k=1
while k<len(list1):
    list2.append(list1[k])
    k+2
print(list2)

