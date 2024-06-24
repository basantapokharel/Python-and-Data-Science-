#passing function as an argument

# def function1():
#     print("Hello from function 1")

# def function2(func):
#     print("Hello from function 2")
#     func()


# function2(function1)

#returning function from another function

# def function3():
#     print("Hello from function 3")

#     def function4():
#         print("Hello from function 4")

#     return function4


# # function3()()

# func_var=function3()
# func_var()



#Decorator
#a decorator is a function that takes another function and extends or alters its behaviour

# def decorator(func):
#     def wrapper():
#         print("Transaction initiated")
#         func()
#         print("Transaction completed")
#     return wrapper

# def hello():
#     print("Transaction is in process")

# decorated_func=decorator(hello)   ## hello function modified by decorator 
# decorated_func()

#shortcut

# @decorator
# def hello():
#     print("Transaction is in process")




# hello()

















# import math

# def square_root(num):

#     sq_root=math.sqrt(num)
#     return sq_root


# #decorator

# def decorator_positive(func):

#     def wrapper(num):

#         if num<0:
#             print("Square root of negative number is not possible")
#             raise ValueError
#         else:
#             sq_root=func(num)
#             return sq_root
#     return wrapper


# using a decorator
# new_decorated_func=decorator_positive(square_root)

# print(new_decorated_func(16))
# print(new_decorated_func(-16)) #returns error


# shorhand decorator to use decorator 


# @decorator_positive
# def area_of_square_land(length):
#     area=length**2
#     return area


# print(area_of_square_land(5))




# import time


# def decorator_time(func):

#     def wrapper():

#         start_time=time.time()   #For example, if time.time() returns a value of 1665043212.1234567, it means that 1,665,043,212 seconds have passed since the Unix epoch (January 1, 1970, 00:00:00 UTC). 
#         func()

#         end_time=time.time()

#         print(end_time-start_time)
#     return wrapper

# @decorator_time
# def function1():
#     print("Hello from function 1")

# function1()

# @decorator_time
# def function2():
#     for i in range(200):
#         print(i)            

# function2()







