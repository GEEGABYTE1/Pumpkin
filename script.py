from block import Block
from blockchain import Blockchain
from datetime import datetime, time
from termcolor import colored

pumpkin = Blockchain()

class Script:
    
    def __init__(self):
        print('-'*24)
        time.sleep(0.4)
        user_input = str(input(': '))
        
        if user_input == 'create_vote':
            self.create_vote()
    
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