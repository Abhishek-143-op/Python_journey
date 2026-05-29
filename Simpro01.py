# building the Calculator 

print("This is the basic calculator [first code without using ai ]]")
a=int(input("Enter the no. 'a' to calculator :"))
b=int(input("Enter the no. 'b'  to calculator :"))

#adding
def add(a,b):
    return a+b

#substraction 
def substraction (a,b):
    return a-b

#multiplication 
def multiplication (a,b):
    return a*b

#Division
def division(a,b):
    return a/b

#exponential 
def exponential(a,b):
    return a**b

# calculator main logic 
def calculator(c):
       if (c=="+"):
           print(add(a,b))
       elif (c=="-"):
           print(substraction(a,b))
       elif(c=="*"):
           print(multiplication(a,b))
       elif(c=="/"):
           print(division(a,b))
       elif(c=="^"):
           print(exponential(a,b))
       else:
           print("Invalid Input")


#creating infinite loop until c=0

while  True :
    c=input("Enter \n + for addition \n - for substraction \n * for multiplication \n / for division \n ^: for exponential  \n Enter '0' for Exit ")
    if( c !="0" ):
        calculator(c)
    else:
        break
    
