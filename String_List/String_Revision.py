#           Revision of the String .  

s='Abhishek' #string

#string slicing 
b=s[0:5] #positive slicing
c=s[-5:-1] #negative slicing 
print(f"printing using string slicing : {b}, {c}")
'''
    b=s[:1000]  print upto the last character from the s 
    b=s[1000:]  nothing will print as there is not index there to print 

    
'''


#string function 

#case conversion 
print(

    s.capitalize(),
    s.title(),
    s.upper(),
    s.lower(),
    s.swapcase(),
)

#imp function to check the lenght
print(len(s))

#finding
print(

s.find("b"),
s.index("i"),
"Abhi"in s ,
s.startswith("Abhi"),
s.endswith("fuck")
)

#whitespace removing and other 

print(
    s.lstrip,
    s.strip,
    s.rstrip
)

#replace and split
print(
    s.replace("Abhi", "yoyo")


)
 #there are many more such function to use them then use 
 #string_variable.____  : This will list all the string funtion by code editor 

 
'''
NOTE :  strings are immutable means whenever we apply string function it creates the new 
        string the made changes there instead of original string 
'''

