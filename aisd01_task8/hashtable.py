class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        index = len(value) % self.size
        return index

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index
        else:
            i = 0
            while i < self.size:
                index += self.step
                if index >= self.size:
                    index = index - self.size
                if self.slots[index] is None:
                    return index
                else:
                    i += 1
            return None

    def put(self, value):
        # записываем значение по хэш-функции
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
        return slot

    def find(self, value):
        # находит индекс слота со значением, или None
        try:
            return self.slots.index(value)
        except ValueError:
            return None
