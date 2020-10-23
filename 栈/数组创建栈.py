class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    # 添加元素
    def push(self, data):
        self.stack.append(data)
        self.size += 1

    # 删除最后一个元素
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise TypeError('范围错误')
        return temp

    # 打印栈
    def __str__(self):
        return f'{self.stack}'

    # 返回栈的最后一项
    def peek(self):
        if self.stack:
            return self.stack[-1]

    # 返回栈是否为空
    def is_empty(self):
        return not bool(self.stack)

    # 返回栈的元素个数
    def sizes(self):
        return self.size


if __name__ == '__main__':
    result = Stack()
    for i in range(5):
        result.push(i)
    result.pop()
    print(result.sizes())
    print(result.peek())
    print(result.is_empty())
    print(result)
