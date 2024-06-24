import csv

#writing a csv file
csv_content=[
    ["Name","Age","Address"],
    ["Basanta",21,"Dhaka"],
    ["Mukesh",22,"Lalitpur"]
]

with open("data_files/example.csv","w",newline="") as file:  #for argument jump use keyword argument
    csv_writer=csv.writer(file)
    csv_writer.writerows(csv_content)

#reading a csv file
with open("data_files/example.csv","r") as file:
    csv_reader=csv.reader(file)  #returns a iterator object
    # print(csv_reader)
    # print(list(csv_reader))    #to convert it into list we use list(csv_reader) now csv_reader is empty 
    csv_content=list(csv_reader)
   

for row in csv_content[1:]:
    print(row)