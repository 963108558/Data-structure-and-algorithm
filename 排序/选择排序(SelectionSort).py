from typing import List
from randomList import randomList


def selectionSort(iList: List[int]):
    if len(iList) <= 1:
        return iList
    for i in range(len(iList) - 1):  # 外层循环控制几轮
        min_index = i  # 指定当前轮排头的元素位置
        for j in range(i + 1, len(iList)):  # 内层循环负责找到最小值索引
            if iList[min_index] > iList[j]:
                min_index = j
        if min_index != i:
            iList[i], iList[min_index] = iList[min_index], iList[i]
    return iList


if __name__ == '__main__':
    for i in range(10):
        iList = randomList.randomList(20)
        print(selectionSort(iList))
