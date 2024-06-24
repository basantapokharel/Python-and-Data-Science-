#creation of list 

# myList=[]  #empty list
# print(myList)
# print(type(myList))

#from list 

# List1=[1,2,3,4,5,6,7,8,9]
# List2=list(List1)
# print(List2)

# #from string
# list3=list("string")
# print(list3)



# fruits=['apple','banana','papaya','orange']
# print(f"Length of fruits list is: {len(fruits)}")
# #list are mutable
# fruits[2]='mango'
# #inserting elements in list
# fruits.append('grapes')

# fruits.insert(1,'kiwi')

# #removing elements from list
# fruits.remove('kiwi') #remove first occurence of value

# print(fruits.pop()) #removes last element and returns it



# fruits.pop(0) #removes at index


# print(fruits)

# #concatenation of list 
# list1=[1,2,3,4,5,6,7,8,9]
# list2=[10,11,12,13,14,15,16,17,18,19,20]
# # list3=list1+list2    #concatenation using +
# # list3=list1.extend(list2).copy()  #This gives error as .extend returns None
# list3=list1.copy()
# list3.extend(list2) #extend is computationally cheaper than + as + is overloaded so much 
# print(list3)


#slicing in list

list1=[1,2,3,4,5,6,7,8,9]

print(list1[0:3])

print(list1[-2:-1])

#specifying stepsize

print(list1[0:9:2])




print(list1[-4:4:-1])

#reverse a list
rev_list=list1[::-1] #using concept of slicing
print(rev_list)

list1.reverse()  #using reverse method
print(list1)



#Nested List
list2=[1,2,3,[4,5,6],7,8,9]
print(f"Length of list2 is: {len(list2)}")
print(list2)
print(list2[3][2])


