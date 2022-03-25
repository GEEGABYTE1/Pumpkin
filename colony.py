
from cgitb import text
from tkinter import E
from block import Block
from script import Script
from seed_blockchain import Blockchain
from random import random, randint
from termcolor import colored
from linkedlist import DoubleLinkedList
import time
from os import system

from datetime import datetime



seed = Blockchain()
transaction_chain = Blockchain()



class Colony:
    
    user = None
    text_colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    cost = 100
    purchased_color = None
    
    def __init__(self):
        self.initialize_chain()
        user_user = str(input('Desired Username: '))
        self.user = user_user.strip(' ')
        print(colored('Successful! You are now named {}'.format(self.user)))
        
        while True:
            user_input = str(input(': '))
            if user_input == '/global_chat':
                server_runtime = GlobalChat()
                server_runtime.chat(runtime=self)
            elif user_input == '/init_vote':
                runtime_vote = Script()
            elif user_input == '/buy':
                buying_session = Buy()
                buying_session.user_buy(runtime=self)
            elif user_input == '/quit':
                break
            else:
                print('You have typed the wrong command')
            
            

            cost_increment = randint(1, 150)
            self.cost += cost_increment - (cost_increment * 0.03)
    
    def initialize_chain(self):
        for colour in self.text_colors:
            transaction = {'Color': colour}
            seed.add_block(transaction)

                

class Buy:

    def user_buy(self, runtime):
        time.sleep(0.2)
        self.view_shop(runtime=runtime)
        time.sleep(0.2)
        user_inter = str(input('Would you like to buy something? (type y/n): '))
        user_inter = user_inter.lower()
        user_inter = user_inter.strip(' ')
        if user_inter == 'n':
            return 
        else:
            user_des_color = str(input('Type your desired colour: '))
            user_des_color = user_des_color.lower()
            user_des_color.strip(' ')
            for block in seed.chain:
                colour_dict = block.transactions
                if len(colour_dict) == 0:
                    continue
                colour_dict_colour = colour_dict['Color']
                if colour_dict_colour == user_des_color:
                    amount_of_cost = block.amount
                    print('{} will be buying {c} for {a}'.format(runtime.user, c=user_des_color, a=amount_of_cost))
                    print('-'*24)
                    user_check = str(input('Would you like to confirm? (type y/n): '))
                    user_check = user_check.strip(" ")
                    user_check = user_check.lower()
                    if user_check == 'y':
                        if runtime.cost >= amount_of_cost:
                            runtime.cost -= amount_of_cost
                            transaction_by_user = {'Color': user_des_color, 'Amount': amount_of_cost}
                            transaction_chain.add_block(transaction_by_user)
                            print(colored('Transaction Sucessful', 'green'))
                            runtime.purchased_color = user_des_color
                        else:
                            print(colored('You do not have enough funds.', 'red'))
                            time.sleep(0.2)
                            print(colored('You have: {} where {} costs: {} '.format(runtime.cost, user_des_color, amount_of_cost), 'red'))
                    else:
                        print(colored('You have left the buying process'))
                        break 
                else:
                    continue 
                      


    def view_shop(self, runtime):
        colors = runtime.text_colors
        print(colored('Current Colour Rates: '), 'Blue')
        for block in seed.chain:
            block_trans = block.transactions
            if len(block_trans) == 0:
                continue
            block_trans_colour = block_trans['Color']
            for colour in colors:
                if colour == block_trans_colour:
                    rate = block.amount
                    print('{}: {}'.format(colour, rate))
                    break 
                else:
                    continue
                    
            

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
                    user_color = 'white'
                    if runtime.purchased_color == None:
                        pass 
                    else:
                        user_color = runtime.purchased_color
                    specified_user = colored(current_data['User'], user_color)
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
        chat.add_to_tail(dictionary)

    
            
    


running = Colony()
print(running)