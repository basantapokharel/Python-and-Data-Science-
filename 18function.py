# def function_name(list_of_parameters):
#     pass

#function to add two numbers

# def add_two_numbers(num1,num2=30):  #num2 is default argument
#     # print(num1)
#     #docstring
#     '''
#     #this docstring is mentioned when we hover over the function name anywhere
#     This function adds two numbers  

#     Arguments:
#     num1,num2

#     Returns:
#     sum
#     '''
#     return num1+num2

# print(f"Add:{add_two_numbers(10,20)}")  #here 10 and 20 are positional arguments

#keyword arguments
# sum=add_two_numbers(num2=10,num1=20)
# print(sum)

# sum2=add_two_numbers(40)
# print(sum2)


#unpacking of list and tuples

# list1=[10,20,30]
# x,y,z=list1
# print(x,y,z)

#we can use * operator to unpack sequence
# list1=[10,20,30,40,50]
# x,*y,z=list1  #any variable can store more than one values in form of list if given *,now it acts as a list,this is called unpacking or args
# print(x,y,z)


# tuple1=(10,20,30)
# a,b,c=tuple1
# print(a,b,c)


#args in function
# #variable number of positional arguments
# def sum(*var):
#     print(type(var))       #since we gave parameters in () it takes var as a tuple instead of list
    
#     sum=0
#     for num in var:
#         sum+=num
#     return sum

# result=sum(10,20,30,40,50,60,70,80,90,100)
# print(result)


#arbitrary arguments
#refers to a function parameter that is not explicitly defined or specified.
#or def function_name(*var):  it can accept any number of values


#kwargs in function
#used to pass variable number of keyword arguments

# def student_details(**kwargs):
#     print(kwargs)       #accepts any number of keyword arguments in dictionary
#     print(type(kwargs))  

#     for key,value in kwargs.items():
#         print(key,value)

# student_details(name="Basanta",age=20,branch="CSE") #for any number of keyword arguments


#args and kwargs in same function

# def student_details(gender,*args,**kwargs):  #kwargs should be the last parameter of the function
#     print(args)       #accepts any number of positional arguments in tuple
#     print(type(args))  

#     print(kwargs)       #accepts any number of keyword arguments in dictionary
#     print(type(kwargs))  


# student_details('male',10,20,30,40,50,60,70,80,90,100,name="Basanta",age=20,branch="CSE")



#lamda function
#can also be called as anonymous function as it has no name

#syntax: lambda arguments:expression
         #lamda arguments:value if condition else else_value


#without using lambda function
# def square(num):
#     return num**2

# square_of_10=square(10)
# print(square_of_10)

#using lambda function
# square=lambda num:num**2   #function is stored in a variable square

# square_of_10=square(10)
# print(square_of_10)


square=lambda num:num**2 if num%2==0 else num**3
print(square(10))
print(square(11))





