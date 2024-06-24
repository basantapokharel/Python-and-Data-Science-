#generators in python

#Generator is a function that returns an iterator


# def my_generator(num):
#     for i in range(num):
#         yield i

# my_iterator=my_generator(5)
# print(my_iterator)
# print(type(my_iterator))  #returns a iterator ie called generator

#accessing generator elements using next()

# print(next(my_iterator)) #returns 0 and removes it from iterator
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#using loop is same as list but it removes after accessing element
# for num in my_iterator:
#     print(num)
# print(next(my_iterator)) #returns error as iterator is empty

#or we can convert it to list

# my_iterator2=list(my_generator(4))
# print(my_iterator2)


#creating generator from generator expression

# my_generator=(i for i in range(5))
# print(my_generator)
# for num in my_generator:
#     print(num)  



