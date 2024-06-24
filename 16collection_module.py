#queue in python
#like we did include in c++, we import the module in python

#import module_name: This syntax imports the entire module named module_name. After importing, you can access the module's functions, classes, and variables using the module's name as a prefix.

#now to access specific modules function or class or variable we can directly import them using following syntax
#from module_name import function_name/class_name/variable_name
#to assign alias to those function_name/class_name/variable_name we can use following syntax
#from module_name import function_name as fn/class_name as cn/variable_name as vn

from collections import deque

my_queue=deque()
my_queue.append(1)  #insetts at last
my_queue.appendleft(2)  #inserts at first

my_queue.pop()  #removes from last

my_queue.popleft()  #removes from first

print(my_queue)

