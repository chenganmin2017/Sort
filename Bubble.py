#coding=utf-8
import os
import sys
import random

"""
排序思想：
它重复地走访要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
例如：源数据为：[36, 98, 23, 8, 98, 33, 60, 7, 75, 96] 共10个数据
第一次比较的数据个数为0-9个数据，他们两两比较，最后把10个数据中最大的数据存储到数据的最后一位
结果为：[36, 23, 8, 98, 33, 60, 7, 75, 96, 98]
第二次比较的数据个数为0-8，因为第一次比较已经把最带的数据放到了最后一位，所以只比较前9个数据
比较的结果为：[23, 8, 36, 33, 60, 7, 75, 96, 98, 98]
第三次比较的数据个数为0-7，因为第二次比较已经把最带的数据放到了最后两位，所以只比较前8个数据
比较的结果为：[8, 23, 33, 36, 7, 60, 75, 96, 98, 98]
依次类推：结果为
[36, 23, 8, 98, 33, 60, 7, 75, 96, 98]
[23, 8, 36, 33, 60, 7, 75, 96, 98, 98]
[8, 23, 33, 36, 7, 60, 75, 96, 98, 98]
[8, 23, 33, 7, 36, 60, 75, 96, 98, 98]
[8, 23, 7, 33, 36, 60, 75, 96, 98, 98]
[8, 7, 23, 33, 36, 60, 75, 96, 98, 98]
[7, 8, 23, 33, 36, 60, 75, 96, 98, 98]
[7, 8, 23, 33, 36, 60, 75, 96, 98, 98]
冒泡排序的平均时间复杂度为O(N^2)
算法优化：
对冒泡排序常见的改进方法是加入标志性变量Bchange，用于标志某一趟排序过程中是否有数据交换。
如果进行某一趟排序时并没有进行数据交换，则说明所有数据已经有序，可立即结束排序，避免不必要的比较过程。
"""

dataList = [random.randint(1,100) for x in range(10)]


def Bubble(data)->list:
    dataTemp = data.copy()
    size = len(dataTemp)
    for outer_loop in range(size):
        Bchange = False
        for inner_loop in range(size-outer_loop-1):
            if dataTemp[inner_loop] > dataTemp[inner_loop+1]:
                dataTemp[inner_loop], dataTemp[inner_loop+1] = dataTemp[inner_loop+1], dataTemp[inner_loop]
                Bchange = True
        print(dataTemp)
        if not Bchange:
            break
    return dataTemp

def main(argc, argv, envp)->None:
    print("源数据为： ", dataList)
    sortdata = Bubble(dataList)
    print("排序后为： ", sortdata)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)




