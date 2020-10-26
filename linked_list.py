class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def add_in_head(self, item: Node):
        if self.head is None:
            self.tail = item
        else:
            item.next = self.head
        self.head = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        founded_nodes = []
        while node is not None:
            if node.value == val:
                founded_nodes.append(node)
            node = node.next
        return founded_nodes

    def delete(self, val, all=False):
        node = self.head
        node_prev = None
        continue_delete = True

        while node is not None and continue_delete:
            if node.value == val:
                continue_delete = all
                node_next = node.next
                if node == self.head:
                    if node_next:
                        self.head = node_next
                    else:
                        self.head = None
                        self.tail = None
                elif node == self.tail:
                    if node_prev:
                        node_prev.next = None
                        self.tail = node_prev
                    else:
                        self.tail = None
                else:
                    if node_prev:
                        node_prev.next = node_next
            else:
                node_prev = node

            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode: Node, newNode: Node):
        node = self.head

        if self.head is None:
            self.add_in_tail(newNode)
        else:
            while node is not None:
                if node == afterNode:
                    node_next = node.next
                    if node == self.tail:
                        self.add_in_tail(newNode)
                    else:
                        if node_next:
                            newNode.next = node_next
                        else:
                            newNode.next = None
                            self.tail =newNode
                        node.next = newNode

                node = node.next
    def insert(self, afterNode: Node, newNode: Node):
        node = self.head

        if self.head is None or afterNode is None:
            self.add_in_head(newNode)
        else:
            while node is not None:
                if node == afterNode:
                    node_next = node.next
                    if node == self.tail:
                        self.add_in_tail(newNode)
                    else:
                        if node_next:
                            newNode.next = node_next
                        else:
                            newNode.next = None
                            self.tail =newNode
                        node.next = newNode

                node = node.next

    @classmethod
    def sum_two_lists(cls, linked_list_1, linked_list_2):
        result_list = cls()

        if linked_list_1.len() == linked_list_2.len():
            node_1 = linked_list_1.head
            node_2 = linked_list_2.head

            while node_1 is not None and node_2 is not None:
                result_list.add_in_tail(Node(node_1.value + node_2.value))
                node_1 = node_1.next
                node_2 = node_2.next

        return result_list

