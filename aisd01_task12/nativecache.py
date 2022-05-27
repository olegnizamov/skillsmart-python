class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        index = len(key) % self.size
        return index

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            self.hits[self.slots.index(key)] += 1
            return True
        return False

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

    def put(self, key, value):
        slot = self.seek_slot(key)
        if slot is None:
            slot = self.min_slot()
            self.hits[slot] = 0
        self.slots[slot] = key
        self.values[slot] = value

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        if self.is_key(key):
            return self.values[self.slots.index(key)]
        return None

    def seek_min_slot(self):
        return self.hits.index(min(self.hits))
