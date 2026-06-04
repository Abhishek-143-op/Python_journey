#---------------Revising Loops-------------------

# we have for loop and while loop 

#   For :
#           use for loop when we know how many times loop need to run 
#   While : 
#           use While loop when we don't know how many times loops will repeat and
#            be know the condition to repeat he loop .



for i in range(5) : #prints 1 for 5 times  i.e 0-4
    print("1") 

#printing multiplication table using loops

n=int(input("Enter the number for generating table : "))

for i in range(1,10+1):
    print(f"{n} * {i} = {n*i}")


for i in range(5):
    for j in range(i):
        print("*", end="")
    print()