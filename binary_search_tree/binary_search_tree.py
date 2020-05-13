"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else: #value greater than or equal to
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # compare value to the currentNode
        # if smaller, go left
        # if bigger. go right
        # if no node to go to, (either left or right)
            # make the new node at that spot



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if target > self.value:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)
        
        # compare value to the currentNode
        # is it equal
        # if smaller, go left
        # if bigger. go right
        # if equal return true

        # if smaller but we can't go left return false
        # if larger but we can't go right, return false
    

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        if self.right is None:
            return max
        if self.right is not None:
            return self.right.get_max()

        ###################################### alternative solution
        # if self.right:
        #     return self.right.get_max()
        # else:
        #     return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
                
            if self.right:
                self.right.for_each(fn)
    

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):  
         if node:
             # if no left it prints the current value
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        if node:
            queue.append(node)
        while len(queue) > 0:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            removed = queue.pop(0).value
            print(removed)

            # print(node.value)
            # self.bft_print(node.left)
            # self.bft_print(node.right)

           

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
                

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.bft_print(node.left)
            
            print(node.value)

            self.bft_print(node.right)



tree = BinarySearchTree(1)
tree.insert(8)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(3)
tree.insert(4)
tree.insert(2)

tree.dft_print(tree)