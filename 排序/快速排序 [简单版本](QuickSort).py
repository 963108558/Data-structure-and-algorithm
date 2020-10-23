from typing import List
from randomList import randomList


def quick_sort(iList: List[int]):
    if len(iList) <= 1:
        return iList
    base = iList[0]
    left = [i for i in iList[1:] if i < base]
    right = [i for i in iList[1:] if i >= base]
    return quick_sort(left) + [base] + quick_sort(right)


if __name__ == '__main__':
    for i in range(1,21):
        iList = randomList.randomList(20)
        print(f'第{i}次的结果为{quick_sort(iList)}')

