class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        item = Node(value)
        node = self.head

        while node is not None:
            if self.compare(node.value, item.value) > -1 and self.__ascending\
                    or self.compare(node.value, item.value) < 0 and not self.__ascending:
                if self.head == node:
                    item.next = self.head
                    self.head.prev = item
                    self.head = item
                else:
                    item.next = node
                    item.prev = node.prev
                    item.prev.next = item
                    node.prev = item
                break
            node = node.next
        else:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if self.__ascending and val < node.value or not self.__ascending and val > node.value:
                break
            elif node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        result = None
        if self.head is None:
            return result
        if self.head.value == val:
            result = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        else:
            current_node = self.head.next
            while current_node is not None:
                if current_node.value == val:
                    if self.tail == current_node:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    result = current_node
                    break
                current_node = current_node.next

        return result

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        result_len = 0
        node = self.head
        while node is not None:
            result_len = result_len + 1
            node = node.next
        return result_len

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1