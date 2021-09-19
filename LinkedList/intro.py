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
        if self.head == key:
            self.head = None
        temp = self.head
        previous = temp
        while temp:
            if temp.data == key:
                previous.next = temp.next
                break
            previous = temp
            temp = temp.next

    def delete_node_position(self, position):
        if position == 0:
            self.head = self.head.next
            return
        temp = self.head.next
        i = 1
        previous = self.head
        while i <= position and temp:
            if i == position:
                previous.next = temp.next
                break
            previous = temp
            temp = temp.next
            i += 1

    def count_items_in_l_list(self):
        temp = self.head
        i = 0
        while temp:
            i += 1
            temp = temp.next
        return i

    # def count_recursively(self):
    #     if self.head

    def search_recursive(self, item, head):
        if head is None:
            return None
        if head.data == item:
            return True
        return self.search_recursive(item, head.next)


if __name__ == '__main__':
    # Start with the empty list
    l_list = LinkedList()

    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    l_list.head.next = second
    second.next = third

    l_list.print_list()
    print("\n\n\n")
    print(l_list.count_items_in_l_list())
    l_list.print_list()
