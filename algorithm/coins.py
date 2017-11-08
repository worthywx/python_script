# coding=utf-8
# Author: Worthy
# Create Time: 2017/11/8 13:46

def coins(values, money, coinUsed):
    """
    :param values:
    :param money:
    :param coinUsed:
    :return:
    """
    for m in range(1, money + 1):
        minCoin = m
        for value in values:
            if value <= m:
                tmp = coinUsed[m - value] + 1
                if minCoin > tmp:
                    minCoin = tmp
        coinUsed[m] = minCoin


if __name__ == '__main__':
    values = [1, 5, 10, 50]
    coinUsed = {}.fromkeys(range(0, 100), 0)
    coins(values, 99, coinUsed)
    print coinUsed
