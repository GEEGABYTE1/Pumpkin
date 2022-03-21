from re import L
from block import Block
from blockchain import Blockchain
from datetime import datetime
import time 
from termcolor import colored
from stack import Stack

pumpkin = Blockchain()
seed = Blockchain()
background_stack = Stack()

class Script:
    
    def __init__(self):
        print('-'*24)
        time.sleep(0.4)
        while True:
            self.add_vote()
            self.print_current_votes()
            user_input = str(input(': '))
            
            if user_input == '/create_vote':
                self.create_vote()
            elif user_input == '/vote':
                self.vote()
            


    def add_vote(self):
    
        if len(pumpkin.chain) < 3:
            for block in pumpkin.chain:
                if len(block.transactions) == 0:
                    continue 
                block_transaction = block.transactions['Message']
                block_vote_count = block.vote_count
                block_dict = {block_transaction: block_vote_count}
                background_stack.push(block_dict) 
        else:
            try:
                for i in range(background_stack.size):
                    random_block = pumpkin.random_dao_selector()
                    if len(random_block.transactions) == 0:
                        pass 
                    
                    random_block_transaction = random_block.transactions
                    random_block_vote_count = random_block.vote_count 
                    random_block_vote = random_block_transaction[0]
                    block_dict = {random_block_vote: random_block_vote_count}
                    background_stack.push(block_dict)
            except:
                print(colored('Error', 'red'))

        if background_stack.size == 0:
            print(colored('No Votes Have Been Made', 'white'))
        else:
            pass
                    

    def print_current_votes(self):
        nodes = []
        try:
            current_node = background_stack.top_item
            while current_node:
                nodes.append(current_node)
                current_node = current_node.get_link()
            
            print('Current Votes:  ')
            print('-'*24)
            for node in nodes:
                block_message = list(node.value.keys())[0]
                block_count = list(node.value.values())[0]
                string = 'Vote: {} -- Count: {}'.format(block_message, block_count)
                print(string)
                print('-'*24)
        except:
            print(nodes)


    def vote(self):
        pass
        
        
        
    
    def create_vote(self):
        try:
            message = str(input("Your Vote Proposal: "))
            message = message.strip(' ')
            time_of_transaction = datetime.now()
            new_transaction = {'Message': message}
            pumpkin.add_block(new_transaction)
            time.sleep(0.2)
            print(colored('Vote successfully deployed', 'green'))
        except:
            print(colored('Vote not successfully deployed', 'red'))
    


        



class Contract:
    pass
            
        


running = Script()