# # Revising the tuples 

# Name=input("Enter the Input Name : ")
# Roll=int(input("Enter The roll NO. : "))
# Course=input("Enter Course name : ")


# #substituing all values in the tuple 

# tuple1=(Name,Roll,Course) #creating input values to tuple 

# tuple1=tuple1+(90,) #This is method used to enter the element into 
#                      #the tuple 
# print(tuple1)

# List = [
#     tuple1
# ]

# print(List)
List_of_tuple=[]
n=int(input("Enter the number Stuents to details :"))
for i in range (1,n+1):
    print(f"-----------Student{i}--------------")
    Name=input("Enter the  Name : ")
    Roll=int(input("Enter The roll NO. : "))
    Course=input("Enter Course name : ")


    tuple1=(Name,Roll,Course) #Converting the detials to tuples
    List_of_tuple.append(tuple1)


print("Student details inside list under tuples each element :",List_of_tuple)
