class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        index = len(key) % self.size
        return index

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        return key in self.values

    def put(self, key, value):
        slot = self.hash_fun(key)
        self.slots[slot] = value
        self.values[slot] = key
        # гарантированно записываем
        # значение value по ключу key

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        if self.is_key(key):
            return self.slots[self.values.index(key)]
        return None
