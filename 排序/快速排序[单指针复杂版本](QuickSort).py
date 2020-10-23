from typing import List
from randomList import randomList


def quick_sort(iList: List[int], start: int, end: int):
    if start >= end:
        return
    middle = partition(iList, start, end)
    quick_sort(iList, start, middle - 1)
    quick_sort(iList, middle + 1, end)


def partition(iList: List[int], start: int, end: int):
    pivot = iList[start]
    slow = start
    for fast in range(start + 1, end + 1):
        if iList[fast] < pivot:
            slow += 1
            iList[fast], iList[slow] = iList[slow], iList[fast]
    iList[start], iList[slow] = iList[slow], iList[start]
    return slow


if __name__ == '__main__':
    iList = randomList.randomList(20)
    quick_sort(iList, 0, len(iList) - 1)
    print(iList)
