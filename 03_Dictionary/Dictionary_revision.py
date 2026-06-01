#       Learning Dictionay 

# starts with {"key":"value"}, contains key value pair , any datatype

dict1={
    "name":"Abhishek",
    "roll_no" : 50
}
 # dict2=dict1.copy   #here we are equating dict to the variable not to dict

#To copy the proper one dict into the another then we do 
dict2=dict1.copy() # () it means copy the dict1 to the dict2 by creating the dictionary



# Dict main builtin functions 
print(dict2.clear() #remove all the items from  the Dictionary
)
print(
dict1.items()# shows all the items from the dict 

)
print(
dict1.keys() # shows all the keys from the dict

)

print(
    dict2.values() #shows all the values of keys 
)

dict1["course"]="Btech CSE" # adding new item

print(
dict1.items()

)

dict1.pop("roll_no") #remove roll_no

dict1["course"]="Btech"#updating course 

dict1.setdefault("roll_no",00) #Setting default value for key

print(
dict1.get("roll_no", ) #gives the default value of key

)

dict1.popitem()# removes the last item from dict 





