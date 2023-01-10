class worker:
    def __init__(self, name, department, how_long, is_old):
        self.name = name
        self.department = department
        self.how_long = how_long
        self.is_old = is_old

    def soon_retire(self):
        if self.how_long >= 5:
            return True
        else:
            return False

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car has already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print('''
start - to start the car
stop - stop the car
quit - to quit
        ''')
    elif command == "quit":
        break
    else:
        print("sorry, I dont understand!")

list =[1,2,3,4]
count = 1;
for i in list:
    if i == 4:
        print("item matched")
        count = count + 1;
        break
print("found at",count,"location");
