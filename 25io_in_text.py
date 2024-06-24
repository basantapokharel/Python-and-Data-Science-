# my_file=open("data_files/example.txt","w") #write mode opens existing file by deleting previous content if not creates new

# my_file.write("Hello world\nI love python\n")

# my_file.close()



#opening file with context manager
 
# with open("data_files/example.txt","a") as file:   #automatically closes file beyond with block
#     file.write("I am learning file operations in python\n")


#reading text file

with open("data_files/example.txt","r") as file:
    # content=file.read()  
    content1=file.readline()  #gives empty as file.read already read the content and moved pointer at empty position
    content2=file.readlines()

# print(content)
print(content1)
print(content2)