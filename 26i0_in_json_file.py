import json  #module  .json is used in data transfer like form filling

#writing json file
# json_data={
#     "name":"Ram",
#     "age":10,
#     "address":"Bhaktapur"
# }


json_data=[]
json_data.append({
    "name":"Geeta",
    "age":20,
    "address":"Lalitpur",
    "city":"Kathmandu"
})
json_data.append({
    "name":"Shyam",
    "age":30,
    "address":"Lalitpur",
    "city":"Kathmandu"
})
with open("data_files/example.json","w") as file:
    json.dump(json_data,file,indent=4)    #json data,file pointer


# with open("data_files/example.json","r") as file:
#     json_data=json.load(file)
#     # print(json_data)


# for record in json_data:
#     # print(record)
#     print(record["name"])


#giving path

# if this file is in same folder as example.json
# with open("example.json","r") as file:  //just name is sufficient
#     json_data=json.load(file)
#     # print(json_data)

# for record in json_data:
#     print(record["name"])




# my_file=open("data_files/example.json","r")

# data=my_file.read()      #this takes each content as string so in loop we can only access character wise
# print (type(data))

# data=json.loads(data)  #this converts json string to python object
# print(type(data))

#or 

# data=json.load(my_file)
# print(type(data))
# print(data)

# print(data)
# for it in data:
#     print(it)

# my_file.close()




#while writing next method to understand

# with open("data_files/example.json","w") as file:
#     # file.write(json_data)  #direct this gives error as write expects string as argument
#     file.write(json.dumps(json_data))   #converts json_data into string before writing  

# also works but use first one instead

