# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        self.values = []
    # ваша реализация хранилища

    def size(self):
        return len(self.values)
        # количество элементов в множестве

    def put(self, value):
       if value not in self.values:
            self.values.append(value)
    # всегда срабатывает

    def get(self, value):
        return value in self.values
        # возвращает True если value имеется в множестве,
        # иначе False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        if value in self.values:
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2):
        result_set = PowerSet()
        if self.size() <= set2.size():
            for value in self.values:
                if set2.get(value):
                    result_set.put(value)
        else:
            for value in set2.values:
                if self.get(value):
                    result_set.put(value)

        # пересечение текущего множества и set2
        return result_set

    def union(self, set2):
        result_set = PowerSet()
        # объединение текущего множества и set2
        for value in self.values:
            result_set.put(value)
        for value in set2.values:
            result_set.put(value)

        return result_set

    def difference(self, set2):
        # разница текущего множества и set2
        result_set = PowerSet()
        for value in self.values:
            if not set2.get(value):
                result_set.put(value)

        return result_set

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for value in set2.values:
            if not self.get(value):
                return False

        return True
