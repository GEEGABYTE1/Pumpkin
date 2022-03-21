
from tkinter import E
from block import Block
from blockchain import Blockchain
from datetime import datetime
import time 
from termcolor import colored
from stack import Stack

pumpkin = Blockchain()
background_stack = Stack()
front_stack = Stack()


class Script:
    vote_count = 0

    def __init__(self):

        while True:
            self.print_vote()
            user_input = str(input(': '))
            user_input = user_input.strip(' ')
            if user_input == '/create_vote':
                self.create_vote()

    
    def create_vote(self):
        if self.vote_count > 3:
            print("You have made too many vote proposals")
        else:
            user_vote = str(input('Please type in your vote: '))
            transaction = {'Message': user_vote}
            pumpkin.add_block(transaction)
            recent_block = None
            for block in pumpkin.chain:
                transaction = block.transactions 
                if len(transaction) == 0:
                    continue 
                else:
                    transaction_message = list(transaction.values())[0]
                    if transaction_message == user_vote:
                        front_stack.push(block)
                        self.vote_count += 1
                    else:
                        continue

    def print_vote(self):
        if len(pumpkin.chain) == 1:
            print(colored('There have not been any votes made yet', 'white'))
        past_numbers = []
        for i in range(3):
            random_idx = pumpkin.random_dao_selector()
            if random_idx == 0:
                continue 
            elif random_idx in past_numbers:
                continue
            else:
                counter = 1
                current_node = front_stack.top_item 
                while current_node:
                    if counter == random_idx:
                        front_stack.push(current_node.get_value())
                        break 
                    else:
                        counter += 1
                        current_node = current_node.get_link()
    


            


     


running = Script()