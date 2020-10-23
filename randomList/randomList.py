import random

def randomList(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,100))
    return list

if __name__ == '__main__':
    print(randomList(6))