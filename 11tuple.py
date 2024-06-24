#creating tuple
tuple1=() #empty tuple
print(tuple1)
print(type(tuple1))

tuple2=(1,2,3,4,5,6,7,8,9,10)
print(tuple2)
print(type(tuple2))


#creating tuple from list
print("creating tuple from list:")
list1=[1,2,3,4,5,6,7,8,9,10]
tuple3=tuple(list1)
print(tuple3)
print(type(tuple3))


#creating tuple from string
print("creating tuple from string:")
str1="Hello World"
tuple4=tuple(str1)
print(tuple4)
print(type(tuple4))

#creating tuple from tuple
print("creating tuple from tuple:")
tuple5=(1,2,3,4,5,6,7,8,9,10)
tuple6=(11,12,13,14,15,16,17,18,19,20)
tuple7=tuple5,tuple6   #for 2d tuple or   tuple8=(tuple5,tuple6)
tuple8=tuple(tuple5)
print(tuple8)
print(tuple7)
print(type(tuple7))


#tuple is immutable

#  tuple1[0]=100
#  print(tuple1)



#tuple in loop

tuple9=(1,2,3,4,5,6,7,8,9,10)

for i in tuple9:
    print(i)

#tuple unpacking

tuple10=(1,2,3,4,5,6,7,8,9,10)

a,b,c,d,e,f,g,h,i,j=tuple10
print(a,b,c,d,e,f,g,h,i,j)
