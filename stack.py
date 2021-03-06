from node import Node
class Stack:
    def __init__(self, top_item=None):
        self.top_item = top_item 
        self.size = 0
        self.limit = 3 
        self.nodes = []

    def is_empty(self):
        if self.size == 0:
            return True 

    def has_space(self):
        if self.limit > self.size:
            return True 

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("The Stack is Empty")

    def push(self, new_value):
        if self.has_space():
            new_node = Node(new_value)
            new_node.set_link(self.top_item)
            self.top_item = new_node 
            self.size += 1
            self.nodes.append(new_value)
        else:
            print("The Stack is Full")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_link()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The Stack is Empty")