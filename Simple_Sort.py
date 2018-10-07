#coding=utf-8

"""
排序思想：
选择排序：每趟从待排序的记录中选出关键字最小的记录，顺序放在已排序的记录序列末尾，直到全部排序结束为止。
简单排序很简单，它的大致处理流程为：
1.从待排序序列中，找到关键字最小的元素；
2.如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；
3.从余下的N-1个元素中，找出关键字最小的元素，重复1.2步，直到排序结束。
例如：有1组数据[95, 47, 70, 80, 95, 23, 74, 15, 53, 41]
1.从0-10找到最小的数，交换到第1位，得到结果：
[15, 47, 70, 80, 95, 23, 74, 95, 53, 41]
2.从1-10找到最小的数，交换到第2位，得到结果：
[15, 23, 70, 80, 95, 47, 74, 95, 53, 41]
依次类推：
第 2次排序后的结果为： [15, 23, 41, 80, 95, 47, 74, 95, 53, 70]
第 3次排序后的结果为： [15, 23, 41, 47, 95, 80, 74, 95, 53, 70]
第 4次排序后的结果为： [15, 23, 41, 47, 53, 80, 74, 95, 95, 70]
第 5次排序后的结果为： [15, 23, 41, 47, 53, 70, 74, 95, 95, 80]
第 6次排序后的结果为： [15, 23, 41, 47, 53, 70, 74, 95, 95, 80]
第 7次排序后的结果为： [15, 23, 41, 47, 53, 70, 74, 80, 95, 95]
第 8次排序后的结果为： [15, 23, 41, 47, 53, 70, 74, 80, 95, 95]
第 9次排序后的结果为： [15, 23, 41, 47, 53, 70, 74, 80, 95, 95]
"""


import sys
import os
import random

dataList = [random.randint(10,100) for x in range(10)]

def Simple_Sort(data)->list:
    dataTemp = data.copy()
    size = len(dataTemp)
    for outer_loop in range(size):
        temp = dataTemp[outer_loop]
        max_flag = outer_loop
        for inner_loop in range(outer_loop+1, size):
            if temp > dataTemp[inner_loop]:
                temp = dataTemp[inner_loop]
                max_flag = inner_loop
        dataTemp[outer_loop], dataTemp[max_flag] = dataTemp[max_flag], dataTemp[outer_loop]
        print("第{:2}次排序后的结果为：".format(outer_loop) ,dataTemp)
    return dataTemp





def main(argc, argv, envp):
    print("源数据为： ", dataList)
    sortdata = Simple_Sort(dataList)
    print("排序后为： ", sortdata)



if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)