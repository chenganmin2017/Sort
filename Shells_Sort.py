#coding=utf-8

"""
排序思想：
希尔(Shell)排序又称为缩小增量排序，它是一种插入排序。它是直接插入排序算法的一种威力加强版。
希尔排序，也称递减增量排序算法，以其设计者希尔（Donald Shell）的名字命名，该算法由1959年公布。
假设有这样一组数[12, 77, 31, 62, 42, 79, 59, 61, 14, 79]，
1.如果我们以步长为5开始进行排序：
12 77 31 62 42
79 59 61 14 79
然后我们对每列进行排序：
12 59 31 14 42
79 77 61 62 79
2.将上述两行数字，依序接在一起时我们得到：[12, 59, 31, 14, 42, 79, 77, 61, 62, 79]
3.然后再以 2 为步长：
12 59
31 14
42 79
77 61
62 79
4.然后我们对每列进行排序：
12 14
31 59
42 61
62 79
77 79
5.将上述两行数字，依序接在一起时我们得到：[12, 14, 31, 59, 42, 61, 62, 79, 77, 79]
6.最后以 1 为步长进行排序(此时就是就是最简单插入排序了)
12, 14, 31, 59, 42, 61, 62, 79, 77, 79
直接插入排序和希尔排序的比较:
1.直接插入排序是稳定的；而希尔排序是不稳定的。
2.直接插入排序更适合于原始记录基本有序的集合。
3.希尔排序的比较次数和移动次数都要比直接插入排序少，当N越大时，效果越明显。
5.直接插入排序也适用于链式存储结构；希尔排序不适用于链式结构。
"""


import sys
import os
import random

dataList = [random.randint(10,100) for x in range(10)]


def Shells_Sort(data)->list:
    dataTemp = data.copy()
    size = len(dataTemp)
    gap = size // 2
    while gap > 0:
        print(gap)
        for outer_loop in range(gap, size):
            inner_loop = outer_loop - gap
            temp = dataTemp[outer_loop]
            #调试使用
            print("outer_loop = {} inner_loop = {} temp = {}".format(outer_loop, inner_loop, temp))
            while inner_loop >= 0:
                if temp < dataTemp[inner_loop]:
                    dataTemp[inner_loop+gap] = dataTemp[inner_loop]
                else:
                    break
                dataTemp[inner_loop] = temp
                inner_loop -= gap
            print(dataTemp)
        gap //= 2
    return dataTemp


def main(argc, argv, envp):
    print("源数据为： ", dataList)
    sortdata = Shells_Sort(dataList)
    print("排序后为： ", sortdata)



if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)