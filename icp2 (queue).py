class Queue(object):
    # 定义一个空队列
    def __init__(self):
        self.items = []
    # 队列(只能在队尾)添加一个元素

    def enqueue(self, item):
        self.items.append(item)
    # 删除队列（只能在对头）一个元素

    def dequeue(self):
        self.items.pop(0)
    # 判断队列是否为空

    def isEmpty(self):
        return self.items == []
    # 清空队列

    def clear(self):
        del self.items

    # 该队列就不存在了，而不是清空元素
    # 返回队列项的数量
    def size(self):
        return len(self.items)
    # 打印队列

    def print(self):
        print(self.items)

    def recent(self):
        return self.items[-1]


if __name__ == '__main__':
    q = Queue()

    print(q.isEmpty())
    print("the  queue is empty, please input: ")
    for i in input().split():
        q.enqueue(i)
    q.print()
    user_choice = input("input your choice, 1 for dequeue, 2 for recent, 3 for enqueue ")
    if user_choice == '1':
        q.print()
        q.dequeue()
        q.print()
    elif user_choice == '2':
        print(q.recent())
    elif user_choice == '3':
        for i in input().split():
            q.enqueue(i)
        q.print()

