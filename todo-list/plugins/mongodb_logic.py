from pymongo import MongoClient as mongodb
from colorama import Fore,Back,Style
from colorama import init


client = mongodb('mongodb://localhost:27017/')
my_database = client['todos']
my_collection = my_database['todo']


class Mongo:
    def __init__(self):
        pass

    def view(self):
        init()
        for todo in my_collection.find({},{"_id":0, "todo":1, "day":1, "time":1}):
            print('-------------------------------------------')
            print(Fore.CYAN+ todo['todo'], todo['day'], todo['time'])
            print(Style.RESET_ALL)

    def insert(self):
        print('-------------------------------------------')
        todo = input('what is your todo?\n')
        print('-------------------------------------------')
        day = input('what day is this due? use(m,t,w,t,f,s,sn)?\n')
        print('-------------------------------------------')
        time = input('what time is this due? ex(12:00pm)?\n')
        print('-------------------------------------------')
        insert_dict = {'todo': todo, 'day': day, 'time': time}
        my_collection.insert_one(insert_dict)
        print('inserted')

    def remove(self):
        print('-------------------------------------------')
        for todo in my_collection.find({},{"_id":0, "todo":1, "day":1, "time":1}):
            print(Fore.CYAN + todo['todo'], todo['day'], todo['time'])
            print(Style.RESET_ALL)
        remove_todo = input('type todo that you want to remove')
        remove_item= {'todo':remove_todo}
        my_collection.delete_one(remove_item)
        print('removed')

