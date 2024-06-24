#finding average of marks
# marks=[10,20,30,40,50,60]
# # avg_mark=sum(marks)/len(marks)  #direct
# avg_mark=0
# for i in marks:
#     avg_mark+=i
# avg_mark=avg_mark/len(marks)
# print(f"Average mark is :{avg_mark}") 


#print multiplication table of a given number

# print("Enter a number")
# a=int(input())

# for i in range(a,a*11,a):
#     print(i)

#cheking for palindrome


# print("Enter any number")

#as a string
# num=input()
# rev=num[::-1]  

# rev=list(num)  
# rev.reverse()

# rev="".join(rev)

#as a number
# num=int(input())
# num1=num
# rev=0
# while num1>0:
#     rem=num1%10
#     rev=rev*10+rem
#     num1=num1//10

# if num==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#finding greatest

# list=[10,20,70,40,50]
# direct
 # print(max(list)) 
# max=0
# for i in list:
#     if i>max:
#         max=i
# print(max)



#peak elements in list

# list=[11,2,3,1,10,8]
# peak_=[]

# for i in range(len(list)):
#     if i==0:
#         if list[i]>list[i+1]:
#             peak_.append(list[i])
#     elif i==len(list)-1:
#         if list[i]>list[i-1]:
#             peak_.append(list[i])   
#     else:
#         if list[i]>list[i-1] and list[i]>list[i+1]:
#             peak_.append(list[i])

# print(peak_)
        
#count number of vowels
# my_str="hari Basyal"
# count=0

# for i in my_str:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
#         count+=1

# print(count)


#sum of digits of a number
# num=10232
# sum=0
# while(num>0):
#     rem=num%10
#     sum+=rem
#     num=num//10

# print(sum)

#roman to integer

# def roman(ch):
#     if ch=='I' or ch=='i':
#         return 1
#     elif ch=='V' or ch=='v':
#         return 5    
#     elif ch=='X' or ch=='x':
#         return 10
#     elif ch=='L' or ch=='l':
#         return 50
#     elif ch=='C' or ch=='c':
#         return 100
#     elif ch=='D' or ch=='d':
#         return 500
#     elif ch=='M' or ch=='m':
#         return 1000
    
# ch=input("Enter any roman number:")

# total=0
# check=1

# for i in range(len(ch)):

#     if check==0:
#         check=1
#         continue
#     if (i<(len(ch)-1) and (roman(ch[i+1])>roman(ch[i]))):   #only if next number is greater than current 
#         #and most importantly check only if the number has more numbers afterward
        
#         total=total+roman(ch[i+1])-roman(ch[i])
#         check=0
#     else:
#         total+=roman(ch[i])  #this case should be in else case as it also includes case of V,X,or xii(last single)
            
# print(total)




#parenthesis checking

#dictionary of opening and closing parenthesis


# dict={'(':')','[':']','{':'}'}

# paren=input("Enter any sequence of parenthesis:")
# check=1
# list=[]

# for i in paren:
#     if i=='(' or i=='[' or i=='{':
#         list.append(i)
    
    
#     elif i==')' or i==']' or i=='}':
#         if ((len(list)==0) or (dict[list[-1]]!=i)):
#             check=0
#             break
#         else:
#             list.pop()
            

# if (check==0 or len(list)!=0):
#     print("Not valid")
# else:
#     print("Valid")



#frequency of each characters in a string

# string1=input("Enter any string:")
# dict={}

# for ch in string1:
#     dict[ch]=string1.count(ch)

# print(dict)

#next method

# for ch in string1:
#     count=0
#     for i in range(len(string1)):  
#         if string1[i]==ch:
#             count+=1
#     dict[ch]=count

# print(dict)
    


dict2={
    "alice":{
        "math":90,
        "english":50,
        "science":90
    },
    "bob":{
        "math":75,
        "english":85,
        "science":95
    },
    "charlie":{
        "math":80,
        "english":90,
        "science":100
    }
}

dict3={}

for key,value in dict2.items():
    total=0
    
    for k,v in value.items():
        
        total=total+v

    total=round(total/3,2)
    dict3[key]=total

print(dict3)
        



    







        


















