#Iterable and Iterator

#Iterable
    #Iterable are those objects whose elements can be accessed one by one
    #Examples:List,Tuple,Set,Dictionary,string
    #Iterables have methods like __iter__() 

#Iterator
    #Iterators are those objects which stores stream of data
    #Iterators have methods like __next__() and __iter__()


# my_list=[1,2,3,4,5]
# #my_list is iterable because we can use it in for loop
# for num in my_list:
#     print(num)

# #my_list as iterator
# my_iterator=iter(my_list)
# print(my_iterator)


# first_element=next(my_iterator)  #returns first element and removes it from iterator
# print(first_element)

# second_element=next(my_iterator)
# print(second_element)

# print(next(my_iterator))

# print(next(my_iterator))

# print(next(my_iterator))

# # print(next(my_iterator))  #returns error as stop iteration

# #converting iterator to list
# iterator2=iter(my_list)
# new_list=list(iterator2)
# print(new_list)


#map function in python
#It is a higher order function which takes two arguments viz.
   #1. function
   #2. iterable
#and applies the function to each element of the iterable and returns the iterator
#usage: We use map function when we have to apply a function to each element of the iterable


#write a function to calculate a square of number and use it to calculate square of each element of the list

# def square(num):
#     return num**2

# my_list=[1,2,3,4,5]
# out_list=[]

# for num in my_list:
#     out_list.append(square(num))

# print(out_list)

#using comprehension

# out_list=[num**2 for num in my_list]
# print(out_list)

#using map for same tasks

# my_list=[1,2,3,4,5]

# out_list=map(square,my_list) #returns iterator of square of each element #(function,iterable)
# out_list=list(out_list)
# print(out_list)

#using lambda function inside map

# my_list=[1,2,3,4,5]

# out_list=map(lambda num:num**2,my_list) #returns iterator of square of each element

#first convers iterable to iterator for memory optimization and passes each element to the function to map at last the iterator is converted to list
# out_list=list(out_list)

# print(out_list)

#using filter function
#it is similar to map function 
#the function which we pass to filter function should retrn boolean value
#filter function returns an iterator that contains only those elements for which the function returns True

# my_list=[1,2,3,4,5,6,7,8,9,10]
# out_list=[]

# def is_even(num):
#     if (num%2==0):
#         return True
#     else:
#         return False
    
# for num in my_list:
#     if is_even(num):
#         out_list.append(num)

# print(out_list)

# #using list comprehension

# out_list=[num for num in my_list if num%2==0]
# print(out_list)


#using filter function

# out_list=list(filter(is_even,my_list))

# print(my_list)

#using lambda function

# out_list=filter(lambda num:num%2==0,my_list)
# out_list=list(out_list)

# print(out_list)


#reduce function

#we have to add all the elements of the list
#using normal loop
# list1=[1,2,3,4,5]
# sum=0
# for num in list1:
#     sum+=num

# print(sum)

#calling function

# def add(num1,num2):
#     return num1+num2

# list2=[1,2,3,4,5]
# sum=0

# for i in range(len(list2)):
#     sum=add(sum,list2[i])

# print(sum)


#using reduce function

# from functools import reduce
# sum=reduce(add,list2)
# print(sum)








