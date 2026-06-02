#     Revision of the tupple 

# it starts with the () , ordered ,************unmutable collection of data**** 
# , any datatype is stored , 

tuple1= () #empty tuple
tuple2=("Abhishek",) #tuple with one element
tuple3=("Abhishek","tushar","Sakhiyan",True, 999.9, 9 , 69 )
tuple3_copy=tuple3.copy
List1=[10, 49, "Abhishek"]
#same wahii there are many tuple function we can use by tuple.___: code editor will display 
# all functions automatically 

print(
    tuple1.count(tuple1) ,#count no. of elements in tuple 
    tuple3.count("Abhishek") #count Abhishek in tuples 3 
)

print(
    len(tuple2), #print length of tuple 
    tuple3.index(True), # Return the index of the element in (____)
    tuple3.max() #Return index of max element  (if all datatypes is int )
                    #same for min element . 

    , Converted_list =list(tuple3_copy) # convert tuple to list 
    , Converted_tuple=tuple(List1) #converting List to tuple 
    
    , Added_tuple =tuple1+tuple2 #Adding 2 tuples 
    
)


# Tuple items using Loops
for items in tuple3:
    print(f"Items in tuple3  : {items}")

#If tuple has only only Real no. 
tuple_numbers=(10, 30 , 150)
Multi_tuple=tuple2*4
print(
    tuple_numbers.sum(), #gives sum of all no. 
    tuple_numbers.max(), # gives max element 
    tuple_numbers.min(),  #Gives min element
    Multi_tuple #prints tuples which is no. of times multiplied

)


#supports tuple slicing 
"""
MOST IMPORTANT USECASE IN FUTURE : 

TUPLES CAN BE USED AS DICTIONARIES KEYS as keys are immutable therefore tuples can be used 

Lists cannot be used as Dict keys  . 

"""




