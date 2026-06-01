


#taking students input from user into empty list

n=int(input("Enter the total no. of students : "))
for i in range (1,n+1)  :

    #Asking student name (input)
    Student_name=input(f"Enter student {i} name : ")
    #printing student i name 
    print(f"Name of Students {1}: {Student_name}")


    #creating empty list for students makrs
    Student_marks_list=[]


    #Asking no. of subjects (input)
    sub=int(input("Enter the no. subjects:"))


                         # #Asking user for subjects name
                         # for j in range (1,sub+1):
#[Check later in v2]     #     sub_name=input(f"Enter the name of subject {i} :")
                         #     subjects.append(sub_name)

                         # print(f"Subject lists : {subjects}")


    #input marks for  subjects 
    for j in range (1,sub+1):
        seprate_marks=int(input(f"Enter {Student_name} marks of subject{j} out of 100:"))
        Student_marks_list.append(seprate_marks)

    print(f"Marks Lists of {Student_name} : {Student_marks_list}")


    '''            done using built in function             '''
    marks_obtained=0
    #finding total marks obtained by students 
    for j in Student_marks_list:
        marks_obtained=marks_obtained+j
    print(f"Total marks obained : {marks_obtained} ")

    #***************IMP**********************************

    '''             done without using builtin function     
    
    with for loop 
    marks_obtained = 0
    for i in range(len(Student_marks_list)):
         marks_obtained = marks_obtained + Student_marks_list[i]
    print(marks_obtained)



    With built-in function
    marks_obtained = sum(Student_marks_list)
    print("marks obtained : ",{marks_obtained})

    

        '''



    #finding percentage 
    percentage = ((marks_obtained)/(100*sub))*100
    print(f"Percentage : {percentage}")


    #Grading each student 
    if(percentage>=90):
        print(f"{Student_name} grade is : O")
    elif(percentage>=80):
        print(f"{Student_name} grade is : A")
    elif(percentage>=70):
        print(f"{Student_name} grade is : B")
    elif(percentage>=60):
        print(f"{Student_name} grade is : C")
    elif(percentage>=50):
        print(f"{Student_name} grade is : P(pass)")
    else:
        print(f"{Student_name} is fail ")





        


