from script import Script
from blockchain import Blockchain
from random import random
from termcolor import colored
import time
from pymongo import MongoClient
from datetime import datetime


seed = Blockchain()



class Colony:
    user = None

    def __init__(self):
        user_user = str(input('Desired Username: '))
        self.user = user_user.strip(' ')
        print(colored('Successful! You are now named {}'.format(self.user)))
        while True:
            
            user_input = str(input(': '))
            if user_input == '/global_chat':
                server_runtime = GlobalChat()
                server_runtime.chat(runtime=self)
            


class GlobalChat():
    cluster = MongoClient('mongodb+srv://user:pass@seed.10ntx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = cluster['seed']['messaging']
    all_messages = db.find({})
    chats = {}
    restart = False
    db.insert_one({'Id': 'First', 'Message': 'Initial', 'Date': 'First', 'Time': 'Beginning'})

    
    def chat(self, runtime):
        while True:
            date = datetime.now().strftime('%x')
            for message in self.all_messages:
                try:
                    if date != message['Date']:
                        print(colored('Today: {}'.format(message['Time']), 'red'))
                    print(colored("{} ~ {}".format(message['Date'], message['Time']), "red"))
                    print(colored("From: ", 'green'), message['Id'])
                    print(colored("Message: ", 'green'), message['Message'])
                    print('-'*25)
                except:
                    pass
            
            
            person = 'Name: {}'.format(runtime.user) 
            message = input('Message: ')
            if message == '/quit':
                break 
            elif message == '/update':
                self.restart()
            else:
                time = datetime.now().strftime("%X")
                msg = {"Id": person, "Message": message, "Date": date, "Time":time}
                self.db.insert_one(msg)
                print('-'*25)
            
    def restart(self):
        print("\n")
        import sys
        print("Updating the database")
        import os
        os.execv(sys.executable, ['python'] + sys.argv)


running = Colony()
print(running)