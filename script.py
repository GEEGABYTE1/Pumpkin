
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
            elif user_input == '/vote':
                self.vote()
            elif user_input == '/quit':
                break
            else:
                print("Incorrect Command")

    
    def vote(self):
        try:
            vote = False
            current_node = self.background_stack.top_item
            user_vote = str(input('Please type in your vote: '))
            user_vote = user_vote.strip(' ')
            while current_node:
                if current_node.get_value() != None:
                    current_node_transaction = current_node.get_value().transactions
                    current_node_message = current_node_transaction['Message']
                    if current_node_message == user_vote:
                        current_node.get_value().vote_count += 1
                        for block in pumpkin:
                            block_transaction = block.transactions
                            block_message = block_transaction['Message']
                            if block_message == current_node_message:
                                block.vote_count += 1
                            else:
                                continue 
                        vote = True
                        break 
                    else:
                        current_node = current_node.get_link()
            
            if vote == False:
                print(colored("Vote was not Successful", 'red'))
            else:
                print(colored('Vote was Successful', 'green'))
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
        self.background_stack = Stack()
        self.front_stack = Stack()
        if len(pumpkin.chain) == 1:
            print(colored('There have not been any votes made yet', 'white'))
    
        elif len(pumpkin.chain) <= 4:
            for block_index in range(len(pumpkin.chain)):
                if block_index == 0:
                    continue 
                else:
                    self.background_stack.push(pumpkin.chain[block_index])
                    continue     
        else: 
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