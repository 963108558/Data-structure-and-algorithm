from randomList import randomList
from typing import List

def re(iList):
    max_num = max(iList)  # 最大值
    min_num = min(iList)  # 最小值
    much_list = len(iList)  # 桶个数
    bad = max_num - min_num  # 极差
    all_list = []  # 总桶
    for count in range(much_list):
        all_list.append([])  # 总桶里面的桶个数

    for num in iList:
        extent = int((num - min_num)*(much_list - 1)/bad)  # 分桶
        all_list[extent].append(num)

    for j in range(len(all_list)):
        all_list[j].sort()

    arr = []
    for first in all_list:
        for second in first:
            arr.append(second)
    return arr

if __name__ =='__main__':
    iList = randomList.randomList(20)
    iList1 = [0.45,0.87,1.2,3.425,0.137,0.365,0.278,0.359,0.67]
    print(re(iList))
    print(re(iList1))