#coding=utf-8

"""
排序思想：
快速排序的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分：
分割点左边都是比它小的数，右边都是比它大的数。
1.先从数列中取出一个数作为基准数
2.分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边
3.再对左右区间重复第二步，直到各区间只有一个数
例如：
数据： [35, 61, 82, 21, 93, 16, 64, 87, 98, 66]
1.选取数据中的第一个数据作为基准数 35
2.遍历数据，把小于基准数据的放到一个列表中，大于等于基准数的放到另一个列表中
运行结果为left:[21, 16] right:[61,82,93,64,87,98,66]
3.递归中重复操作步骤2
"""


import sys
import os
import random


dataList = [random.randint(10,100) for x in range(10)]

def sortfun(_data):
    if len(_data) <= 1:
        return _data
    else:
        Temp = _data[0]
        left = [x for x in _data[1:] if x <Temp]
        right = [x for x in _data[1:] if x >= Temp ]
        LL = sortfun(left)
        LR = sortfun(right)
    return LL + [Temp] + LR


def Simple_sort(data)->list:
    dataTemp = data.copy()
    return sortfun(dataTemp)


def main(argc, argv, envp):
    print("源数据为： ", dataList)
    sortdata = Simple_sort(dataList)
    print("排序后为： ", sortdata)



if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)
