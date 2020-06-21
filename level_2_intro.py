print("""

Welcome to the jungle!

This is level 2. You know what's going on by now. There are big bad trolls about. 
They really don't like you and its up to you to defend your honor.
Although they they hit like a truck, they're pretty slow and attack every other turn. 
Good luck on your adventuring, it isn't going to last long. 


""")
Continue = input("To continue, hit enter")

if str(Continue) == str():
    exec(open("level_2.py").read())