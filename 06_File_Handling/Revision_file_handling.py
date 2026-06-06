#--------------File Handling -------------------

# It allow user to store data permanently in disk .

"""
--------------Manual Method(file closing done manually) -------------------
file opening : file = open("filename", "mode ") any files can be opened
                                        |-"r" read mode 
                                        |-"w" write mode 
                                        |-"r+" read write mode 
                                        |-"a" append file 
                                        |-"x" create new file 

file closing : file.close()

file closing must be necessary otherwise resource will still be occupied by code 

--------------Automatic fileclosing mething (Prefered)---------------


with open("file_name","mode") as __anything__:
    print(__anithing__) or #code like loop condition 


"""
# it creates the example.txt file in the main folder
'''file1=open("example.txt", "x") ''' 

#Reading the data from the file
file1=open("06_File_Handling/example.txt","r")
content=file1.read()
print(content)
file1.close()








