# x=10
# y=20.5

# a=x+y
# print(a)
# print(type(a))

# a=x/y
# print(a)
# print(type(a))

# a=x//y    #returns floor value only after division
# print(a)
# print(type(a))

# a=x**y
# print(a)
# print(type(a))

# a=x%y
# print(a)
# print(type(a))

# z=10+3j
# print(z)

# z=complex(x,y)
# print(z,type(z))


z1=complex(20,30)
z2=complex(10,5)
z3=z1 * z2
print(z3)


#Boolean DataType


a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(a ^ b) #xor 

def xnor(x,y):
    return not (x^y)

print(xnor(a,b)) #xnor


