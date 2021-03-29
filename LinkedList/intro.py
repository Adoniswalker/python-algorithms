class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_after(after_node, data):
        temp_node = after_node.next
        new_node = Node(data)
        after_node.next = new_node
        new_node.next = temp_node

    def insert_item_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        new_node = Node(key)
        if self.head is None:
            return
        temp = self.head
        previous = temp
        while temp:
            if temp.data == key:
                previous.next = temp.next
            previous = temp
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    l_list = LinkedList()

    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    l_list.head.next = second
    second.next = third

    l_list.print_list()
    l_list.insert_after(second, 7)
    l_list.print_list()
