from singly_linked_list import Node
from singly_linked_list import SingleListLink
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         return self.storage.append(value)


#     def pop(self):
#         return self.storage.pop()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = SingleListLink()

    def __len__(self):
        self.size = self.storage.get_max()
        return self.size

    def push(self, value):
        return self.storage.add_to_tail(value)


    def pop(self):
        return self.storage.remove_last_item()
       
     

