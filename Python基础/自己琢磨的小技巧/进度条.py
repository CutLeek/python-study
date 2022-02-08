#!/usr/bin/python3
import time

def com_progress(percent):
    """
    进度条
    :param percent: 已完成lenth / 总lenth
    :return: [##################################################] 100%
    """
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '#'
    print('\r[%-50s] %d%%' % (res, int(100 * percent)), end='')
com_progress(0.1)
time.sleep(1)
com_progress(0.2)

