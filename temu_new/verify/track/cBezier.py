"""
author: cbb
这个库基于贝塞尔曲线实现模拟人手动滑动的轨迹
可以用于selenium轨迹的模拟，或者生成轨迹数组用于js加密通过网站服务器后端分控检测
QQ群 134064772
里面的人说话好听，个个都是人才
"""
import numpy as np
import math
import random


class bezierTrajectory:
    def _bztsg(self, dataTrajectory):
        lengthOfdata = len(dataTrajectory)

        def staer(x):
            t = (x - dataTrajectory[0][0]) / (
                dataTrajectory[-1][0] - dataTrajectory[0][0]
            )
            y = np.array([0, 0], dtype=np.float64)
            for s in range(len(dataTrajectory)):
                y += dataTrajectory[s] * (
                    (
                        math.factorial(lengthOfdata - 1)
                        / (math.factorial(s) * math.factorial(lengthOfdata - 1 - s))
                    )
                    * math.pow(t, s)
                    * math.pow((1 - t), lengthOfdata - 1 - s)
                )
            return y[1]

        return staer

    def _type(self, type, x, numberList):
        numberListre = []
        pin = (x[1] - x[0]) / numberList
        if type == 0:
            for i in range(numberList):
                numberListre.append(i * pin)
            if pin >= 0:
                numberListre = numberListre[::-1]
        elif type == 1:
            for i in range(numberList):
                numberListre.append(1 * ((i * pin) ** 2))
            numberListre = numberListre[::-1]
        elif type == 2:
            for i in range(numberList):
                numberListre.append(1 * ((i * pin - x[1]) ** 2))

        elif type == 3:
            dataTrajectory = [
                np.array([0, 0]),
                np.array([(x[1] - x[0]) * 0.8, (x[1] - x[0]) * 0.6]),
                np.array([x[1] - x[0], 0]),
            ]
            fun = self._bztsg(dataTrajectory)
            numberListre = [0]
            for i in range(1, numberList):
                numberListre.append(fun(i * pin) + numberListre[-1])
            if pin >= 0:
                numberListre = numberListre[::-1]
        numberListre = np.abs(np.array(numberListre) - max(numberListre))
        biaoNumberList = (
            (numberListre - numberListre[numberListre.argmin()])
            / (
                numberListre[numberListre.argmax()]
                - numberListre[numberListre.argmin()]
            )
        ) * (x[1] - x[0]) + x[0]
        biaoNumberList[0] = x[0]
        biaoNumberList[-1] = x[1]
        return biaoNumberList

    def getFun(self, s):
        """

        :param s: 传入P点
        :return: 返回公式
        """
        dataTrajectory = []
        for i in s:
            dataTrajectory.append(np.array(i))
        return self._bztsg(dataTrajectory)

    def simulation(self, start, end, le=1, deviation=0, bias=0.5):
        """

        :param start:开始点的坐标 如 start = [0, 0]
        :param end:结束点的坐标 如 end = [100, 100]
        :param le:几阶贝塞尔曲线，越大越复杂 如 le = 4
        :param deviation:轨迹上下波动的范围 如 deviation = 10
        :param bias:波动范围的分布位置 如 bias = 0.5
        :return:返回一个字典equation对应该曲线的方程，P对应贝塞尔曲线的影响点
        """
        start = np.array(start)
        end = np.array(end)
        cbb = []
        if le != 1:
            e = (1 - bias) / (le - 1)
            cbb = [[bias + e * i, bias + e * (i + 1)] for i in range(le - 1)]

        dataTrajectoryList = [start]

        t = random.choice([-1, 1])
        w = 0
        for i in cbb:
            px1 = start[0] + (end[0] - start[0]) * (
                random.random() * (i[1] - i[0]) + (i[0])
            )
            p = np.array([px1, self._bztsg([start, end])(px1) + t * deviation])
            dataTrajectoryList.append(p)
            w += 1
            if w >= 2:
                w = 0
                t = -1 * t

        dataTrajectoryList.append(end)
        return {
            "equation": self._bztsg(dataTrajectoryList),
            "P": np.array(dataTrajectoryList),
        }

    def trackArray(
        self, start, end, numberList, le=1, deviation=0, bias=0.5, type=0, cbb=0, yhh=10
    ):
        """

        :param start:开始点的坐标 如 start = [0, 0]
        :param end:结束点的坐标 如 end = [100, 100]
        :param numberList:返回的数组的轨迹点的数量 numberList = 150
        :param le:几阶贝塞尔曲线，越大越复杂 如 le = 4
        :param deviation:轨迹上下波动的范围 如 deviation = 10
        :param bias:波动范围的分布位置 如 bias = 0.5
        :param type:0表示均速滑动，1表示先慢后快，2表示先快后慢，3表示先慢中间快后慢 如 type = 1
        :param cbb:在终点来回摆动的次数
        :param yhh:在终点来回摆动的范围
        :return:返回一个字典trackArray对应轨迹数组，P对应贝塞尔曲线的影响点
        """
        s = []
        fun = self.simulation(start, end, le, deviation, bias)
        w = fun["P"]
        fun = fun["equation"]
        if cbb != 0:
            numberListOfcbb = round(numberList * 0.2 / (cbb + 1))
            numberList -= numberListOfcbb * (cbb + 1)

            xTrackArray = self._type(type, [start[0], end[0]], numberList)
            for i in xTrackArray:
                s.append([i, fun(i)])
            dq = yhh / cbb
            kg = 0
            ends = np.copy(end)
            for i in range(cbb):
                if kg == 0:
                    d = np.array(
                        [
                            end[0] + (yhh - dq * i),
                            ((end[1] - start[1]) / (end[0] - start[0]))
                            * (end[0] + (yhh - dq * i))
                            + (
                                end[1]
                                - ((end[1] - start[1]) / (end[0] - start[0])) * end[0]
                            ),
                        ]
                    )
                    kg = 1
                else:
                    d = np.array(
                        [
                            end[0] - (yhh - dq * i),
                            ((end[1] - start[1]) / (end[0] - start[0]))
                            * (end[0] - (yhh - dq * i))
                            + (
                                end[1]
                                - ((end[1] - start[1]) / (end[0] - start[0])) * end[0]
                            ),
                        ]
                    )
                    kg = 0

                y = self.trackArray(
                    ends,
                    d,
                    numberListOfcbb,
                    le=le,
                    deviation=0,
                    bias=0.5,
                    type=0,
                    cbb=0,
                    yhh=2,
                )
                s += list(y["trackArray"])
                ends = d
            y = self.trackArray(
                ends,
                end,
                numberListOfcbb,
                le=le,
                deviation=0,
                bias=0.5,
                type=0,
                cbb=0,
                yhh=0,
            )
            s += list(y["trackArray"])

        else:
            xTrackArray = self._type(type, [start[0], end[0]], numberList)
            for i in xTrackArray:
                s.append([i, fun(i)])
        return {"trackArray": np.array(s), "P": w}


def get_track(distance):
    def __ease_out_expo(sep):
        if sep == 1:
            return 1
        else:
            return 1 - pow(2, -10 * sep)

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(
            f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}"
        )
        # 初始化轨迹列表
    slide_track = []
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    ptime = slide_track[-1][-1]
    return slide_track


class Models_m:
    def __init__(self, x, y, time, t):
        self.x = x
        self.y = y
        self.time = time
        self.t = t


def _genModel_m(startTime, startX, startY, replys):
    list_m = []

    list_m.append(Models_m(startX, startY, startTime, 0).__dict__)
    random_generator = random.Random()

    for i, reply in enumerate(replys):
        if i % 2 != 0:
            continue

        x = reply["x"] + startX
        y = int(
            random_generator.choice(
                [startY + random.randint(1, 10), startY + random.randint(1, 10)]
            )
        )
        time = reply["relative_time"] + startTime

        list_m.append(Models_m(x, y, time, 0).__dict__)

    return list_m


bt = bezierTrajectory()
if __name__ == "__main__":
    bt = bezierTrajectory()
    d = bt.trackArray(
        [random.randint(300,400), random.randint(100,150)],
        [224.7, 57.7],
        numberList=random.randint(40,50),
        le=10,
        type=3,
        bias=0.9,
        deviation=100,
        cbb=2,
        yhh=200,
    )

    trackArray = [[int(x), int(y)] for x, y in d["trackArray"]]
    import time
    print(trackArray)
    mel = []
    for i in trackArray:
        time.sleep(random.randint(10, 25) / 1000)
        mel.append(
            [
                i[0] + 0.7,
                i[1] + 0.7,
                int(time.time() * 1000),
            ]
        )
    print(mel)