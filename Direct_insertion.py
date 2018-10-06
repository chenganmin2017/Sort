#coding=utf-8

"""
排序思想：
每一次循环将一个待排序的数据，按照其数据的大小插入到有序队列的合适位置里，直至全部插入完成。
假设有一组无序序列 R0, R1, ... , RN-1。
(1)我们先将这个序列中下标为 0 的元素视为元素个数为 1 的有序序列。
(2)然后，我们要依次把 R1, R2, ...,RN-1 插入到这个有序序列中。所以，我们需要一个外部循环，从下标 1 扫描到 N-1 。
(3)接下来描述插入过程。假设这是要将 Ri 插入到前面有序的序列中。由前面所述，我们可知，插入Ri时，前 i-1 个数肯定已经是有序了。
所以我们需要将Ri 和R0 ~ Ri-1 进行比较，确定要插入的合适位置。这就需要一个内部循环，我们一般是从后往前比较，即从下标 i-1 开始向 0 进行扫描。
例如：源数据为 [43, 27, 49, 41, 30, 54, 11, 29, 74, 41]
第一次取源数据得第二位27，与源数据的前1个数据比较,得到的结果为：[27, 43, 49, 41, 30, 54, 11, 29, 74, 41]
第二次取源数据的第三位49，与源数据的前2个数据比较，得到的结果为：[27, 43, 49, 41, 30, 54, 11, 29, 74, 41]
第三次取源数据的第四位41，与源数据的前3个数据比较，得到的结果为：[27, 41, 43, 49, 30, 54, 11, 29, 74, 41]
依次类推，最终得到排序
"""

import sys
import os
import random

dataList = [random.randint(10,100) for x in range(10)]

def Direct_insertion(data)->list:
    dataTemp = data.copy()
    size = len(dataTemp)
    for outer_loop in range(1,size):
        temp = dataTemp[outer_loop]
        print("The temp is {}".format(temp))
        print("The outer_loop is {}".format(outer_loop))
        inner_loop = outer_loop
        """
        这是简化后的
        while inner_loop > 0 and temp < dataTemp[inner_loop-1]:
            dataTemp[inner_loop] = dataTemp[inner_loop-1]
            inner_loop -= 1
        dataTemp[inner_loop] = temp
        """
        while inner_loop > 0:
            if temp < dataTemp[inner_loop-1]:
                dataTemp[inner_loop] = dataTemp[inner_loop - 1]
            else:
                break
            inner_loop -= 1
        else:
            pass
        dataTemp[inner_loop] = temp
        print(dataTemp)
        print(' ......... ')
    else:
        pass
    return dataTemp



def main(argc, argv, envp)->None:
    print("源数据为： ", dataList)
    sortdata = Direct_insertion(dataList)
    print("排序后为： ", sortdata)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)
