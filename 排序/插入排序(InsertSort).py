from typing import List
from randomList import randomList


def insertSort(iList: List[int]):
    if len(iList) <= 1:
        return iList
    for right in range(1, len(iList)):
        target = iList[right]
        for left in range(right):
            if iList[left] > target:
                iList[left + 1:right + 1] = iList[left:right]
                iList[left] = target
                break
    return iList


if __name__ == '__main__':
    for i in range(10):
        iList = randomList.randomList(20)
        print(insertSort(iList))
