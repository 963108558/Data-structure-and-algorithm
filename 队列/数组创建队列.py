class Queue:
    def __init__(self):
        self.entries = []
        self.size = 0

    def enqueue(self, data):
        self.entries.append(data)
        self.size += 1

    def dequeue(self):
        temp = self.entries[0]
        self.entries = self.entries[1:]
        self.size -= 1
        return temp

    def get(self, index):
        for i in range(index+1):
            current = self.entries[i]
        return current

    def sizef(self):
        return self.size

    def __repr__(self):
        printed = ""
        printed += "<" + str(self.entries)[1:-1] + ">"
        return printed

    def reverse(self):
        self.entries = self.entries[::-1]


if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    queue.dequeue()
    print(queue.get(4))
    queue.reverse()
    print(queue)
