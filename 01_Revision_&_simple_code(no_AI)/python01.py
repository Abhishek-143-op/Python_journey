# variables ,
#  literals(fixed no. directly written in code) , 
# whitespace,
#  keywords(reserved words), 
# token(smallest unit of code or set of character ) , 
# indentifiers  (UserDefined i.e name of varible given by the user )
# Delimiters : symbols  used to separate piece of code i.e (), [], {} , ; , : , . etc

print("hello world ")
a = 10  # int variable 
a = "hello" # string variable 
print(a) 
print(type(a))

b="python"
print(b[0:3])


'''         OPERATORS        '''
#Arithmatic operators : +, - , *, **, / ,//, % : Arithmatics operators 
#comparisinoal operators : == , += , -= , *= , **= , // 
#logical : and , or , not 
# memebership operators : in and not in 
# identity operators : is and is not 


'STUDY THIS ABOVE LATER'
# bitwise : &(and) ,`(or) , ^(xor), ~(negation), <<(left shift ), >> (right shift )



#binary , decimal , oxtcal , hexdecimal 
z= 0xA # hexadecimal 
# for later on
print(z)


# Creating function 
def greet (name ="user"):
    print(f"gooooood boi {name}")

#calling function 
greet() #without argument 
greet("MOMO") #with argument

#returning value to funtion
def add(a,b): # whole add function value will become a+b
    return a+b


#conditional statement 
'Normal conditional statement'
    # if(condition):
    #     #code
    #     else:
    #         #code

'leader conditional satement'
# if (condition 1 ):
#     code1
# elif(condition 2 ):
#     code2
#     .
#     .
# else : 
#     coden

'nested conditional statement'
# if (condition_main ):
#     if(condition1.1):
#         code1.1
#     else:
#             code1.n


'loops '

#basic loop
print("output using simple for loop ")
for i in range (1,10):
    print(i)

#creating infinite loop 
while True:
    #code 
    pass
    break # must req. otherwise infinite loop will be created 

#nested loop 
print("output using nested loop ")
for i in range (1,5):
    for j in range (1,5):
        print(j,end="")
    print("")

#basic while loop 
print("using while loop printing 1-9")
i=1 #initilization 
while i!=10 :#condition 
    print(i) #code 
    i = i+1 #updation 



