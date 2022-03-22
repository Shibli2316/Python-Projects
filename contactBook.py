class ContactBook():
    def __init__(self, name: str, phone:int):
        self.name=name
        self.phone=phone
        print(f"A contact with name {self.name} is created")

def createContact():
    newContactName=str(input("Enter the name of the person: "))
    newContactNumber=int(input("Enter the number: "))
    new=ContactBook(newContactName, newContactNumber)
    with open("ContactBook.txt", "a") as f:
        f.write('\n')
        f.write(newContactName)
        f.write('\t')
        f.write(str(newContactNumber))

# contactList=[contactList.append(newContactName)]

def deleteContact():
    deleteName=str(input("Enter the name you want to delete: "))
    with open ("ContactBook.txt") as f:
        contacts=f.read().lower()
        if deleteName in contacts:                                
            contacts=deleteName.replace(deleteName, "####")
            with open("ContactBook.txt", 'w') as f:
                f.write(contacts)
        else:
            print("Contact unavailable")


def findContact():
    find=str(input("Enter the name you want to find: "))
    # print(find)
    contact=True
    i=1
    with open ("ContactBook.txt") as f:
        while contact:
            contact=f.readline().lower()
            if 'Ilma' in contact:
                print(f"The contact {find} is at line {i}")
            i+=1
            # else:
            #     print("Contact unavailable, to add the contact go back to the menu and press 1.")

while True:
    print("Welcome to the  commmunity contact page. Here are your options")
    print("\tPress 1 to add a contact")
    print("\tPress 2 to delete a contact")
    print("\tPress 3 to find a contact")
    print("\tPress 4 to exit")
    userInput=int(input("Enter yor choice: "))
    if userInput==1:
        createContact()
    elif userInput==2:
        deleteContact()
    elif userInput==3:
        findContact()
    elif userInput==4:
        print("Thanks for choosing us")
        exit()
    else:
        print("Invalid Input")
