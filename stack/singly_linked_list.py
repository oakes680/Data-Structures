class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SingleListLink:
    def __init__(self):
        self.head = None
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def remove_head(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value
    def get_max(self):
        current = self.head
        length = 0
        while current is not None:
            length +=1
            current = current.next
        return length

    def remove_last_item(self):
        
        if self.head is None:
            return None
        else:
            current = self.head
            previous = current
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
        return current.value


# singleList = SingleListLink()
# singleList.append(10)
# singleList.append(11)
# singleList.append(12)
# print(len(singleList))
# print(singleList.head.next.next.value)
# print('this is the last item', singleList.remove_last_item())

# print(singleList.head.value)


            