#coding=utf-8
import os
import sys
import random

dataList = [random.randint(1,100) for x in range(10)]


def Bubble(data)->list:
    dataTemp = data.copy()
    size = len(dataTemp)
    for outer_loop in range(size):
        Bchange = False
        print("第{}执行....".format(outer_loop))
        for inner_loop in range(size-outer_loop-1):
            # print(inner_loop, end = ' ')
            if dataTemp[inner_loop] > dataTemp[inner_loop+1]:
                dataTemp[inner_loop], dataTemp[inner_loop+1] = dataTemp[inner_loop+1], dataTemp[inner_loop]
                Bchange = True
            print("第{0}次循环，第{1}次比较".format(outer_loop,inner_loop),dataTemp)
        if not Bchange:
            break
    return dataTemp

def main(argc, argv, envp)->None:
    sortdata = None
    print("源数据为： ", dataList)

    sortdata = Bubble(dataList)
    # print(Bubble(dataList))
    print("排序后为： ", sortdata)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv, os.environ)


