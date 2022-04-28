from deque import Deque


def is_polindrome(str):
    is_string_polindrome = True
    deque = Deque()
    for char in str:
        deque.addTail(char)
    while deque.size() > 1 and is_string_polindrome:
        if deque.removeTail() != deque.removeFront():
            is_string_polindrome = False

    return is_string_polindrome


if __name__ == '__main__':
    stackqueue = Deque()
    print(is_polindrome("aabna"))