class Stack(object):
    # 定义一个空栈
    def __init__(self):
        self.items = []
    # 添加一个元素

    def push(self, item):
        self.items.append(item)
    # 删除一个元素

    def pop(self):
        return self.items.pop()
    # 返回栈顶

    def top(self):
        return self.items[-1]

    # 判断是否为空

    def is_empty(self):
        return self.items == []
    # 返回栈中元素个数

    def size(self):
        return len(self.items)
    # 打印栈

    def print(self):
        print(self.items)


if __name__ == '__main__':

    s = Stack()
    print(s.is_empty())
    print("the stack is empty, please input: ")
    for i in input().split():
        s.push(i)
    s.print()
    user_choice = input("input your choice, 1 for pop, 2 for top, 3 for push ")
    if user_choice == '1':
        s.print()
        s.pop()
        s.print()
    elif user_choice == '2':
        print(s.top())
    elif user_choice == '3':
        for i in input().split():
            s.push(i)
        s.print()








