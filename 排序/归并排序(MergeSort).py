from typing import List
from randomList import randomList


def mergeSort(iList: List[int]):
    if len(iList) <= 1:
        return iList
    middle = len(iList) // 2
    left, right = iList[0:middle], iList[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left: List[int], right: List[int]):
    arr = []
    while left and right:
        if left[0] > right[0]:
            arr.append(right.pop(0))
        else:
            arr.append(left.pop(0))
    if left:
        arr.extend(left)
    if right:
        arr.extend(right)
    return arr


if __name__ == '__main__':
    for i in range(1, 21):
        iList = randomList.randomList(20)
        print(f'第{i}次排序{mergeSort(iList)}')
