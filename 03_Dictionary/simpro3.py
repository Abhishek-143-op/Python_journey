# In this i will try to create The phone book without AI 


'''
Inputs : person can enter the input name of contact and phone no. 
            name - key 
            phone no. - value
        
features : search 
            update
            delete 

output : person can see phone book and perform operation 

'''

#Empty Dictionary
phone_book={}


#add Contact
def add_contact():
    Name=input("Enter the name of person : ")
    Phone_num=int(input("Enter the Phone no. : "))
    phone_book[Name]=Phone_num

    
# Searching
def search():
    Search_name=input("Enter the name to search: ")
    if Search_name in phone_book:
        print(phone_book[Search_name])
    else:
        print("Contact not found ")

#deleting 

def delete():
    Deleting_name=input("Enter the name to Delete: ")
    if Deleting_name in phone_book:
        phone_book.pop(Deleting_name)
    else:
        print(f"{Deleting_name} is not exits in Contact")

#updating

def update():
    Update_num=int(input("Enter the phone no. : "))
    Update_name=input("Enter the name of which you want to update contact: ")
    if Update_name in phone_book:
        phone_book[Update_name]=Update_num
    else:
        print(f"{Update_name} donot exits in Contact")

def view():
    print("Phone Book  : ",phone_book)





while True:
    print(
    """ 
==========Phone Book ==================
        1. Add Contact
        2. Search Contact
        3. Update Contact
        4. Delete Contact
        5. View Contacts
        6. Exit """
)
    choice=int(input("Enter the choice : "))
    if choice==1:
        add_contact()
    elif choice==2:
        search()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        view()
    elif choice==6: 
        break
    else:
        print("Invalid Input")