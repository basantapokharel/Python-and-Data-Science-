import json

with open("data_files/students.json","r") as file:
    json_data=json.load(file)

# print(json_data)


for record in json_data:
    total=sum(record['marks'])
    percentage=total/4
    record['percentage']=percentage
    

with open("data_files/students_update.json","w") as file:
    json.dump(json_data,file)


with open("data_files/students_update.json","r") as file:    
    json_data=json.load(file)
    # print(json_data)

count_fail=0
count_first_div=0
count_sec_div=0
count_third_div=0
count_distinction=0

for record in json_data:
    if record["percentage"]<40: 
        count_fail+=1
    elif record["percentage"]>=40 and record["percentage"]<50:
        count_third_div+=1
    elif record["percentage"]>=50 and record["percentage"]<65:
        count_sec_div+=1
    elif record["percentage"]>=65 and record["percentage"]<80:
        count_third_div+=1
    else:
        count_distinction+=1


print(f"Total number of students are {len(json_data)}")
print(f"Number of students who failed is {count_fail}")
print(f"Number of students who got distinction is {count_distinction}")
print(f"Number of students who got 1st division is {count_first_div}")
print(f"Number of students who got 2nd division is {count_sec_div}")
print(f"Number of students who got 3rd division is {count_third_div}")


    
        
    