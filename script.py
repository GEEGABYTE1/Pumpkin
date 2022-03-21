from re import L
from turtle import back
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
    backlog_track = []
    
    def __init__(self):
        print('-'*24)
        time.sleep(0.4)
        while True:
            self.homescreen_stack = Stack()
            self.homescreen_vote()
            self.print_current_votes()
            user_input = str(input(': '))
            
            if user_input == '/create_vote':
                self.create_vote()
            elif user_input == '/vote':
                result = self.vote()
                pass 
            else:
                print("Invalid Command")



    def homescreen_vote(self):
        indices = []
        for i in range(3):
            random_block = pumpkin.random_dao_selector()
            indices.append(random_block)
        
        for block in indices:
            self.homescreen_stack.push(block)
        
        



    def add_vote(self, transaction):

        if len(pumpkin.chain) == 1:
            print(colored('No Votes Have Been Made', 'white'))
        else:
            transaction_message = transaction['Message']
            background_stack.push(transaction_message)
            

    def update_val(self, transaction_new):
        current_node = background_stack.top_item 
        while current_node:
            transaction = current_node.value
            transaction_message = list(transaction.keys())[0]
            if transaction_new == transaction_message:
                return current_node 
            else:
                continue 
        
            


    def find_votes(self):
        current_node = background_stack.top_item
        lst = []
        while current_node:
            transaction = current_node.value
            transaction_message = list(transaction.keys())[0]
            lst.append(transaction_message)
            current_node = current_node.get_link()
        return lst
            
                    

    def print_current_votes(self):
        nodes = []
        try:
            current_node = self.homescreen_votescreen_stack.top_item
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
        if len(self.backlog_track) != 0:
            print("You have already voted! ", 'white')
            return None
        else:
            user_num = int(input('Please choose a number from 1 - 3 for the corresponding vote you would like to give: '))
            if user_num > background_stack.size:
                print("That number does not correspond to a vote")
            else:
                current_node = background_stack.top_item
                desired_vote = None
                count = 1
                while current_node:
                    if count == user_num:
                        desired_vote = current_node 
                        break
                    else:
                        count += 1
                        current_node = current_node.get_link()
                
                desired_vote.value[list(desired_vote.value.keys())[0]] += 1
                target_val = list(desired_vote.value.keys())[0]
                vote = None
                for block in pumpkin.chain:
                    if len(block.transactions) == 0:
                        continue 
                    else:
                        transaction = list(block.transactions.values())[0]
                        if transaction == target_val:
                            block.vote_count += 1
                            vote = True
                        else:
                            continue 
                if vote == True:
                    print(colored('Voted {} successfully!'.format(target_val), 'green'))
                    self.backlog_track.append(target_val)
                else:
                    print(colored('Vote Error!'.format(target_val), 'red'))

        


    
    def create_vote(self):
        try:
            message = str(input("Your Vote Proposal: "))
            message = message.strip(' ')
            time_of_transaction = datetime.now()
            new_transaction = {'Message': message}
            pumpkin.add_block(new_transaction)
            time.sleep(0.2)
            self.add_vote(new_transaction)
            print(colored('Vote successfully deployed', 'green'))
        except:
            print(colored('Vote not successfully deployed', 'red'))
    


        



class Contract:
    pass
            
        


running = Script()