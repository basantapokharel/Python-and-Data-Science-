list_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_square_of_num=[]

# for num in list_of_num:
#     list_of_square_of_num.append(num**2)

# print(list_of_square_of_num)

# note
# list_of_square_of_num=[0]*len(list_of_num)  #initializes with all zero with size equal to len(list_of_num)
# for i in range(len(list_of_num)):
#     list_of_square_of_num[i]=list_of_num[i]**2  
# print(list_of_square_of_num)

# using list comprehension
# list_of_square_of_num=[expression for item in sequence]

# list_of_square_of_num=[num**2 for num in list_of_num]
# print(list_of_square_of_num)


# list_of_square_of_even_num=[num**2  for num in list_of_num if num%2==0]
###list_of_square_of_even_num=[expression if condition else else_expression for item in sequence]
list_of_square_of_even_num=[num**2 if num%2==0 else num for num in list_of_num]
print(list_of_square_of_even_num)


# #without using set comprehension

# set_of_squares_of_numbers=set()

# for num in list_of_num:
#     set_of_squares_of_numbers.add(num**2)

# print(set_of_squares_of_numbers)

#using set comprehension

# set_of_squares_of_even_numbers={num**2 for num in list_of_num if num%2==0}
# print(set_of_squares_of_even_numbers)


original_dict = {'a': 1, 'b': 2, 'c': 3}
#without using dictionary comprehension swapping keys and values

#print(original_dict.items())  #gives list of tuples

# new_dict={}
# for key,value in original_dict.items():   #gives tuple but then tuple unpacking occurs such that key and value gets respective value
#     new_dict[value]=key
# print(new_dict)


#using dictionary comprehension

#syntax: new_dict={key:expression for key,value in dict.items() if condition}
# new_dict={value:key for key,value in original_dict.items()}
# print(new_dict)


dict_2={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}


#new dictionary with only key values where value is even and store values by squaring

# new_dict={key:value**2 for key,value in dict_2.items() if value%2==0}
# print(new_dict)










