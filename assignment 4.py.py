import copy 
"""
#Q1:-reverse the whole list using list method,
a=[1,2,3,4,5,6,7]
a.reverse()
print(a)
#Q.2- Print all the uppercase letters from a string.
lst=['A','B','c','d']
for i in range(0,len(lst)):
    if lst[i].isupper()==True:
        print(lst[i])
"""
#Q.3- Split the user input on comma's and store the values in a list as integers.
lst=[]
b=0
strg=input("Enter the number")
strg1=strg.split(',')
for i in range(0.len(strg1)):
    b=int(strg1[i])
    lst.append(b)
    print("list:"lst)

#Q.4- Check whether a string is palindromic or not.
strg=input("Enter the string")
strg1=strg[::-1]
    if strg==strg1:
        print("string is palindromic")
        else:
            print("string is not palindromic")
"""

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
lst=[1,2,[3,4],5]
lst1=copy.deepcopy(lst)
lst1[2][0] = 4
print(lst)
print(lst)

