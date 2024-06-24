string1="Hello World"
print(string1)

string2='Hello World2'
print(string2)

string3="Ram's"
print(string3)

string4='''Ram is a boy'''
print(string4)

#accessing characters of a string
first=string1[4]
print(first)

last=string1[-1]
print(last)

#slicing    

sliced=string1[0:5]
print(sliced)


#looping 
for char in string1:
    print(char)


#length of string
print(len(string1))


#concatenation

string5=string1+string2
print(string5)


#repetation

string6=string1*3
print(string6)


#membership

print('World' in string1)  #returns true if 'World' is present in string1

#immutable

#string1[0]='H'  #strings are immutable

#methods of strings
string7="hello world,how are you"
print("Mehods of string")

#upper

print(string7.upper()) #all in caps

#lower

print(string7.lower()) #all in small

#title

print(string7.title()) #first letter of each word in caps


#split

print(string7.split(',')) #splitting string by comma,returns list
print(string7.split())   #by default delimiter is space

#strip()

print(string7.strip())  #removes leading and trailing(after end of string) spaces   

#find()

print(string7.find('w'))  #returns index of first occurence of w
print(string7.find('ld'))  #returns index of first occurence of o
print(string7.find('mango'))  #returns -1 if not found












