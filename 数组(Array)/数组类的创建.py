class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity  # 数组的容量
        self.size = 0  # 有效的元素个数

    # 添加元素
    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError('索引错误')
        if index >= len(self.array) or self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    # 删除元素
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('索引错误')
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    # 增添数组容量
    def addcapacity(self):
        # 创建新数组
        new_array = [None] * len(self.array) * 2
        # 把旧数组的内容复制到新数组里
        for i in range(self.size):
            new_array[i] = self.array[i]
        # 定义新数组
        self.array = new_array

    # 打印数组
    def __repr__(self):
        return f'{self.array}'


if __name__ == '__main__':
    result = Array(10)
    for i in range(10):
        result.insert(i, i)
    result.insert(2, 3)
    result.insert(2, 4)
    result.insert(2, 5)
    result.remove(3)
    print(result)
