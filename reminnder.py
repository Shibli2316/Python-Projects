import datetime
print(datetime.datetime.now())

with open('List.txt', 'w') as f:
    f.write("This is the list of reminders that you have set\n")



class Entries():
    def __init__(self, reminder_name, reminder_time):
        self.name= reminder_name
        self.time= reminder_time

    def prntDetails(self):
        return f'You are setting a reminder at {datetime.datetime.now()} and your reminder for {self.name} has been set for {self.time}'

print("Welcome to my reminder program")
print("What would you like to do\n\tPress 1 to add reminder, or\n\tPress 2 to see the lists of reminders.")

a=int(input("Entre the number you want to proceed with: "))
if a==1:
    print('To add a reminder please write its name and the time at which you would like us to remind you')
    x=input("Entre a proper name for the reminder:\n")
    y=input("Entre the time (in 24 hrs format) at which you want to be reminded:\n")
    z='.txt'
    c=x+z
    with open(c,'w') as f1:
        f1.write(f'You set a reminder for {x} at {datetime.datetime.now()}')
        f1.write('\n')
        # f1.seek()
    with open(c,'a') as f2:
        f2.write(f'your first reminder for {x} will be relayed at {y}')
    with open('List.txt','a') as f3:
        f3.write(x)
        f3.write('\n')
        f3.write(y)
        f3.write('\n')
    first=Entries(x, y)
    print(first.__dict__)
    print(first.prntDetails())

if a==2:
    with open('List.txt','r') as f:
        print(f.read())