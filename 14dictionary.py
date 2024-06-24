#creating a empty dictionary

dict1={}

print(dict1)
print(type(dict1))

#non empty dictionary
student={
    "name":"Basanta",
    "age":20,
    "branch":"CSE",
    "courses":["C","C++","Java","Python"]
}
print(student)

#accessing elements of dictionary

print(student["name"])
print(student["age"])
print(student["branch"])
print(student["courses"])

#accessing using get

print(student.get("name"))
print(student.get("age"))
print(student.get("branch"))
print(student.get("courses"))

#this method is used to provide default value if key is not present

print(student.get("address","Not found"))


#length of dictionary

print(len(student)) #returns the number of elements in dictionary


#adding elements in dictionary
student["address"]="Dhaka"
print(student)

#updating elements in dictionary
student["age"]=21
print(student)


#removing elements in dictionary
del student["address"]
print(student)


#clearing dictionary

# student.clear()
# print(student)

#methods of dictionary

#keys

print(student.keys()) #returns the list of keys

#values

print(student.values()) #returns the list of values

#items

print(student.items()) #returns list of tuples


#copy

dict2=student.copy()
print(dict2)


#update

dict2.update(student) #updates dict2 with student
print(dict2)


#pop

dict2.pop("name") #removes the element with key name
print(dict2)


#looping

for key,value in student.items():
    # key,value=i   #tuple unpacking
    print(key,value)


#membership

print("name" in student) #returns true if 'name' is present in student

#looping over two lists of same length, zip

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]

for i,j in zip(list1,list2):
    print(i,j)




