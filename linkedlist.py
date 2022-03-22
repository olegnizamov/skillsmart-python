class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
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
        result = []

        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result  # здесь будет ваш код

    def delete(self, val, all=False):
        result = None
        if self.head is None:
            return result
        if self.head.value == val:
            result = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current_node = self.head.next
            prev_node = self.head
            while current_node is not None:
                if current_node.value == val:
                    if self.tail == current_node:
                        self.tail = prev_node
                        self.tail.next = None
                    else:
                        prev_node.next = current_node.next
                    result = current_node
                    break
                prev_node = current_node
                current_node = current_node.next

        if (all is True) and (result is not None):
            self.delete(val, True)

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result_len = 0
        node = self.head
        while node is not None:
            result_len = result_len + 1
            node = node.next
        return result_len

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код
