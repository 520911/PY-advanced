class Stack:
    def __init__(self, *args):
        self.data = [*args]

    def isEmpty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if len(self.data) > 0:
            last = self.data[-1]
            self.data.pop()
            return last

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]

    def size(self):
        return len(self.data)


def check_balance(string):
    stack = Stack()
    open_list = tuple("[{(")
    close_list = tuple("]})")
    zipped = dict(zip(open_list, close_list))
    for i in string:
        if i in open_list:
            stack.push(zipped[i])
        elif i in close_list:
            if not stack.size() or i != stack.pop():
                return False
    return True


balance = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
not_balance = ['}{}', '{{[(])]}}', '[[{())}]']


if __name__ == '__main__':
    for i in balance + not_balance:
        print('Сбалансированно' if check_balance(i) else 'Несбалансированно')
