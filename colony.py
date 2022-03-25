from tokenize import Double
from script import Script
from blockchain import Blockchain
from random import random
from termcolor import colored
from linkedlist import DoubleLinkedList
import time
from os import system

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
            

chat = DoubleLinkedList()
class GlobalChat():

    def chat(self, runtime):
        date = datetime.now()
        string_date = date.strftime('%x')
        current_node = chat.head_node 
        if current_node == None:
            print(colored("There are no chats", 'red'))
            dictionary = {'Message': 'Beginning of Chat', 'Date': string_date, 'User': 'Headless Horseman'}
            chat.add_to_head(dictionary)
            print(colored('Initial Chat Room Initialized', 'green'))
        else:
            while current_node:
                if current_node.get_value() != None:
                    current_data = current_node.get_value()
                    message = colored(current_data['Message'], 'white')
                    date = colored(current_data['Date'], 'yellow')
                    specified_user = colored(current_data['User'], 'blue')
                    print('\n')
                    print(specified_user)
                    print(colored('*'*len(specified_user), 'white'))
                    print('{}: {}'.format(date, message))     
                    time.sleep(0.1)
                    print('-'*24)
                    
                    current_node = current_node.get_link()
                else:
                    current_node = current_node.get_link()

            self.add_to_chat(string_date=string_date, runtime=runtime)
            system('clear')

                    



            
    def add_to_chat(self, string_date, runtime):
        user_message = str(input(''': '''))
        user_user = runtime.user
        dictionary = {'Message': user_message, 'Date': string_date, 'User': user_user}
        chat.add_to_head(dictionary)

    
            
    


running = Colony()
print(running)