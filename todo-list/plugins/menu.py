from time import sleep as wait
from plugins.mongodb_logic import Mongo
from plugins.banner import Banner





class Menu:
    def __init__(self):
        pass

    def menu(self):
        print('''
            [0]- Remove todos
            [1]- Create todos
            [2]- View todos
            [3]- Set reminders 
        ''')
        userInput = int(input('what would you like to do?'))
        if userInput == 0:
            Mongo().remove()
            wait(2.5)
            Banner().banner()
            Menu().menu()
        elif userInput == 1:
            Mongo().insert()
            wait(2.5)
            Banner().banner()
            Menu().menu()
        elif userInput == 2:
            Mongo().view()
            wait(2.5)
            Banner().banner()
            Menu().menu()
        else:
            Menu().menu()



