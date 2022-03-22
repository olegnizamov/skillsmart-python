from linkedlist import LinkedList, Node


# 1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка) insert(afterNode, newNode)
# Если afterNode = None, добавьте новый элемент первым в списке.

# * 1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению delete(val, all=False)
    # где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    # 1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
    my_list = LinkedList()
    my_list.add_in_tail(Node(11))
    my_list.add_in_tail(Node(11))
    my_list.print_all_nodes()
    print('---------------------')
    my_list.delete(11, True)
    my_list.print_all_nodes()
    print('---------------------')

    # 1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()
    my_list = LinkedList()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(11))
    my_list.add_in_tail(Node(12))
    result_len = my_list.len()
    print(result_len)
    print('---------------------')

    # 1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()
    my_list = LinkedList()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(11))
    my_list.add_in_tail(Node(12))
    my_list.print_all_nodes()
    my_list.clean()
    my_list.print_all_nodes()
    print('---------------------')


    # 1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов). find_all(val)
    my_list = LinkedList()
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(11))
    my_list.add_in_tail(Node(12))
    my_list.add_in_tail(Node(10))
    my_list.add_in_tail(Node(11))
    my_list.add_in_tail(Node(12))
    my_list.add_in_tail(Node(13))
    my_list.print_all_nodes()
    result = my_list.find_all(12)
    print('---------------------')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
