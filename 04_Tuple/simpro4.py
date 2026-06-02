#           SIMPLE STUDENT DATABASE MANAGEMENT



def input_details ():


    Name=input("Enter Student name : ")
    Rollno=int(input("Enter Student Roll No.  : "))
    Course=input("Enter Course : ")
    Total_marks=int(input("Enter Total marks : "))

    Details={
        "name":Name,
        "Rollno":Rollno,
        "Course":Course,
        "Total_marks":Total_marks
    }

    return Details

# Student1=input_details()
# print(Student1)

Total_stud=int(input("how many students recorde you want to enter : "))

Student_database={}

for i in range(1,Total_stud+1):
    print(f"\n--------Students{i}----------")
    Student_record=input_details()
    Roll_number_key=Student_record["Rollno"]
    Student_database[Roll_number_key]=Student_record


for key, value in Student_database.items():
    print(f"\n-------Student{i}-------")
    print("database Key: ", key )

    print("Name :", value["name"])
    print("Roll:", value["Rollno"])
    print("Course:",value["Course"])
    print("Total Marks : ", value["Total_marks"])



# Student_database[Student1["Rollno"]]=Student1 #dict_name[key]=value used to add key value pair to dictionaries

#we made key = variable i.e changes a/c to user 
#by taking key as input from input_detailes returned dictionary






