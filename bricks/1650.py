# -*- coding: utf-8 -*-


def busyStudent(startTime, endTime, queryTime):
    r = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime <= endTime[i]:
            r = r + 1
    return r


if __name__ == '__main__':
    # startTime = [1, 2, 3]
    # endTime = [3, 2, 7]
    # queryTime = 4

    startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    queryTime = 5

    print(busyStudent(startTime, endTime, queryTime))
