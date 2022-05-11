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
        slot = self.hash_fun(value)
        if self.slots[slot] is not None and value != self.slots[slot]:
            start_seek = slot
            is_end = False
            while self.slots[slot] is not None:
                slot = (slot + self.step) % self.size
                if slot <= start_seek:
                    is_end = True
                if is_end and slot >= start_seek:
                    return None
        return slot

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
