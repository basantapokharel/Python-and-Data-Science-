#creating set
my_set=set()   #my_set={}is considered as dictionary
print(my_set)
print(type(my_set)) 


#creating set takes unique elements

set1={1,2,3,4,5,6,7,8,9,6,10,10}
# print(set1)

#adding elements

# set1.add(11)

# print(set1)

# #removing elements

# set1.discard(11)  #if 11 is not a members do nothing,not available in list
# print(set1)

# set1.remove(10)   #if 10 is not a members throw error
# print(set1)

# set1.pop()   #removes random element as set is unordered
# print(set1)

#operations in sets

set2={1,2,3,4,5,6,7,8,9}

#union
print("union")
set3=set1.union(set2)
print(set3)

#intersection
print("intersection")
set4=set1.intersection(set2)
print(set4)

#difference
print("difference")
set5=set1.difference(set2)
print(set5)


#use case of set

list1=["ram","shyam","hari","geeta"] #students of a class
list2=["ram","nirmal","sita","geeta"] #passed students of school

set6=set(list1)
set7=set(list2)

set8=set6.intersection(set7) #students who passed from a class
list3=list(set8)
print(list3)


#set is mutable but it can be made immutable called frozen-set
set9=frozenset(set3)
print(set9)
print(type(set9))

