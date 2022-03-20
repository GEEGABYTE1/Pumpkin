from re import L
from block import Block
from blockchain import Blockchain
from datetime import datetime, time
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
            self.print_current_votes()
            user_input = str(input(': '))
            
            if user_input == '/create_vote':
                self.create_vote()
            elif user_input == '/vote':
                self.vote()
            


    def add_vote(self):
        try:
            for i in range(background_stack.size):
                random_block = pumpkin.random_dao_selector()
                random_block_transaction = random_block.transactions
                random_block_vote_count = random_block.vote_count 
                random_block_vote = random_block_transaction[0]
                background_stack.push(random_block_vote)
        except:
            print(colored('Error', 'red'))
                
    

    

    def print_current_votes(self):
        nodes = []
        current_node = background_stack.top_item
        while current_node.get_link() != None:
            nodes.append(current_node)
            current_node = current_node.get_link()
        
        print('Current Votes:  ')
        print('-'*24)
        for node in nodes:
            print(node)

            



    def vote(self):
        pass
        
    
    def create_vote(self):
        try:
            message = str(input("Your Vote Proposal: "))
            message = message.strip(' ')
            time_of_transaction = datetime.now()
            new_transaction = {str(time_of_transaction): message}
            pumpkin.add_block(time_of_transaction)
            time.sleep(0.2)
            print(colored('Vote successfully deployed', 'green'))
        except:
            print(colored('Vote not successfully deployed', 'red'))
    


        



class Contract:
    pass
            
        


running = Script()