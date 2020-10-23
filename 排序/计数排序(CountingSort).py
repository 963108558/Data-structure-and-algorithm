from typing import List
from randomList import randomList


def couunt_sort(iList: List[int]):
    if len(iList) <= 1:
        return iList
    max_num = max(iList)
    count = [0]*(max_num + 1) #[0,0,0,0,0,0,0,0,0,0] 记录各个数字的次数
    for element in iList:
        count[element] +=1
    arr = []
    for i in range(max_num+1): #  出现的数字:  0 -- max_num+1
        for j in range(count[i]): # 遍历次数
            arr.append(i)
    return arr

if __name__ == '__main__':
    iList = randomList.randomList(20)
    print(couunt_sort(iList))



