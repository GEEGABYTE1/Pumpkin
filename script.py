
from tkinter import E
from block import Block
from blockchain import Blockchain
from datetime import datetime
import time 
from termcolor import colored
from stack import Stack

pumpkin = Blockchain()
background_stack = Stack()



class Script:
    vote_count = 0

    def __init__(self):

        while True:
            self.print_vote()
            user_input = str(input(': '))
            user_input = user_input.strip(' ')
            if user_input == '/create_vote':
                self.create_vote()
            if user_input == '/vote':
                self.vote()

    
    def vote(self):
        try:
            current_node = self.front_stack.top_item
            while current_node:
                if current_node.get_value() != None:
                    pass
        except:
            print(colored("There are currently no votes made", 'red'))

    
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
                        self.front_stack.push(block)
                        self.vote_count += 1
                    else:
                        continue

    def print_vote(self):
        if len(pumpkin.chain) == 1:
            print(colored('There have not been any votes made yet', 'white'))
        self.background_stack = Stack()
        self.front_stack = Stack()
        for i in range(3):
            random_block = pumpkin.random_dao_selector()
            if random_block == None:
                continue 
            else:
                if random_block in self.background_stack.nodes:
                    pass 
                else:
                    self.background_stack.push(random_block)
        
        current_node = self.background_stack.top_item 
        while current_node:
            if current_node.get_value() != None:
                block = current_node.get_value()
                block_message = block.transactions['Message']
                block_vote = block.vote_count 
                print('Vote Proposal : {} || Vote Count: {}'.format(block_message, block_vote))
                current_node = current_node.get_link()
            else:
                break


            


     


running = Script()
print(running)