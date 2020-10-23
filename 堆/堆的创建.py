class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        """
        先把元素放在最后,然后从后往前依次堆化
        这里以大堆顶为例,如果插入元素比父节点大,则交换,直到最后
        """
        self.data_list.append(data)
        index = len(self.data_list) - 1  # 新添加(最后一个)元素的索引
        parent = self.get_parent_index(index)
        # 循环,直到该元素成为堆顶,或小于父节点(对于大堆顶)
        while parent is not None and self.data_list[index] > self.data_list[parent]:
            self.swap(index, parent)  # 交换操作
            index = parent  # 节点上移
            parent = self.get_parent_index(parent)

    def inserts(self, *value):
        for data in value:
            self.insert(data)

    def pop(self):
        remove_node = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapity(0)
        return remove_node

    def heapity(self, index):
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2*index+1 <= total_index and self.data_list[index] < self.data_list[2*index+1]:
                maxvalue_index = 2*index+1
            if 2*index+2 <= total_index and self.data_list[index] < self.data_list[2*index+2]:
                maxvalue_index = 2*index+2
            if maxvalue_index == index:
                break
            self.swap(index,maxvalue_index)
            index = maxvalue_index



if __name__ == '__main__':
    heap = Heap()
    heap.inserts(10,9,8,7,6,5,4,3,2,1)
    # heap.swap(6,4)
    heap.pop()
    print(heap.data_list)
