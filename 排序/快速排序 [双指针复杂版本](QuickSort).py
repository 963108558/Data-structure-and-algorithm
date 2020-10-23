from typing import List
from randomList import randomList


def swap(iList: List[int], a: int, b: int):
    iList[a], iList[b] = iList[b], iList[a]


def quick_sort(iList: List[int], start: int, end: int):
    if start >= end:
        return
    middle = partition(iList, start, end)
    quick_sort(iList, start, middle - 1)
    quick_sort(iList, middle + 1, end)


def partition(iList: List[int], start: int, end: int):
    pivot = iList[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and iList[p] < pivot:
            p += 1
        while p <= q and iList[q] >= pivot:
            q -= 1
        if p < q:
            swap(iList, p, q)
    swap(iList, start, q)
    return q


if __name__ == '__main__':
    iList = randomList.randomList(20)
    quick_sort(iList,0,len(iList)-1)
    print(iList)
