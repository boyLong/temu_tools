# -*- coding: utf-8 -*-

import re
from captcha.img_corlor import get_color
import uuid
import os
import cv2
import numpy as np
import math
from captcha.predict import Predict
import requests
from collections import Counter


class TextObj:
    unique = None  # 是否唯一
    point = {}  # { "color": "红", "type": "字",""}  # 数字|字母|几何体
    transit = {}  # 过渡中间属性, {"color": "红", "type": "字", ,"category": “接近", "value"}
    order = []

    def get(self):
        return {"unique": self.unique, "point": self.point, "transit": self.transit, "order": self.order}


class Semantic:
    def __init__(self, text):
        self.text = text.strip()
        self.text_obj = TextObj()
        self.color = "yellow|red|green|blue|gray"
        self.type = "number|letter|geometry|object"

    def parse(self):
        if "Please click in order" in self.text:
            self.text_obj.order = self.text.split(":")[-1].strip().split()
            return self.text_obj
        if 'the unique object' in self.text:
            self.text_obj.unique = True
            return self.text_obj
        info = re.findall(f"Please click on ({self.color}) ({self.type})", self.text)
        if info:
            self.text_obj.point = {"color": info[0][0], "type": info[0][1]}
            return self.text_obj

        info = re.findall(f"Please click on all (tilted|duplicate) ({self.type})", self.text)
        if info:
            self.text_obj.point = {"category": f"all {info[0][0]}", "type": info[0][1]}
            return self.text_obj
        info = re.findall(f"Please Click the ({self.type}) nearest from ({self.type}) '(\w)'", self.text)
        if info:
            self.text_obj.point = {"type": info[0][0]}
            self.text_obj.transit = {"type": info[0][1], "value": info[0][2], "category": "nearest"}

            return self.text_obj
        info = re.findall(f"Please click on the (lowercase|uppercase) corresponding to the ({self.color}) letter",
                          self.text)
        if info:
            self.text_obj.point = {"type": info[0][0]}
            self.text_obj.transit = {"color": info[0][1], "type": "letter", "category": "corresponding"}
            return self.text_obj
        info = re.findall(f"Please click on the ({self.type}) closest to ({self.color}) ({self.type})", self.text)
        if info:
            self.text_obj.point = {"type": info[0][0]}
            self.text_obj.transit = {"color": info[0][1], "type": info[0][2], "category": "closest"}
            return self.text_obj
        info = re.findall(f"Please click the (smaller|larger) ({self.color}) (\w+)", self.text)
        if info:
            self.text_obj.point = {"category":info[0][0],"type": info[0][2], "color": info[0][1]}
            return self.text_obj
        # 新的逻辑
        info = re.findall(f"Please click all (smaller|larger) ({self.color}) (\w+)", self.text)
        if info:
            self.text_obj.point = {"category": f'all {info[0][0]}', "color": info[0][1], "type": info[0][2]}
            return self.text_obj
        info = re.findall(f"Please click on all (lowercase|uppercase) letters corresponding to the single letter",self.text)

        if info:
            self.text_obj.point = {"type": f"{info[0]}"}
            self.text_obj.transit = {"type": "letter", "category": "corresponding", "verb": "single"}
            return self.text_obj
        info = re.findall(f"Please click the ({self.color}) ({self.type}) to the (right|left|behind|in front) [(of |\S)]*the object that appears once",self.text)
        if info:
            self.text_obj.transit = {"category": info[0][2], "type": "object", "verb": "once"}
            self.text_obj.point = {"color": info[0][0],  "type": info[0][1],}
            return self.text_obj
        info = re.findall(f"Please click on the ({self.type}) (above|below) (\w+)",self.text)
        if info:
            self.text_obj.transit = {"category": info[0][1], "type": info[0][2]}
            self.text_obj.point = {"type": f"{info[0][0]}"}
            return self.text_obj
        info = re.findall(f"Please click on all other ({self.type}) with the same shape as the ({self.color}) ({self.type})", self.text)
        if info:
            self.text_obj.transit = {"category": "same", "color": info[0][1], "type": info[0][2]}
            self.text_obj.point = {"type": info[0][1]}
            return self.text_obj
        info = re.findall(f"Please click on the (unrotated|rotated) (letter|digit)", self.text)
        if info:
            if info[0][1] == "digit":
                self.text_obj.point = {"type": "number"}
            else:
                self.text_obj.point = {"type": "letter"}
            self.text_obj.point["category"] = info[0][0]
            return self.text_obj

        with open("未适配的文本.txt", "a", encoding="utf-8") as f:
            f.write(self.text)
        raise TypeError("未适配的文本")


class Identity:

    def __init__(self,image,model_cls=1):
        self.image = image
        self.tmp_img = f"{uuid.uuid4()}.jpg"
        self.predict = Predict(self.image, model_cls)
    def draw_image(self, coordinate):
        nparr = np.frombuffer(self.image, np.uint8)
        # image = cv2.imread(self.image)
        image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

        if coordinate["rotation"]:

            rect = ((coordinate['box_mid_xy'][0], coordinate['box_mid_xy'][1]),
                    (coordinate["width"] - 7, coordinate["height"] - 7), coordinate["rotation_origin"])
            box = cv2.boxPoints(rect)
            box = np.intp(box)
            rect = cv2.minAreaRect(box)
            center, size, theta = rect

            x, y = center
            w, h = size
            if theta < -45:
                theta += 90

            # 使用 OpenCV 进行图像剪裁
            # img = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
            # img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            rows, cols = image.shape[:2]
            M = cv2.getRotationMatrix2D(center, theta, 1)
            img_rotated = cv2.warpAffine(image, M, (cols, rows))

            # 根据旋转后的矩形信息进行剪裁
            cropped_image = cv2.getRectSubPix(img_rotated, (int(w), int(h)), (x, y))

            cv2.imshow(coordinate["label_name"], cropped_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

        # 定义四个点坐标
        x1, y1, x2, y2 = coordinate["xyxy"]

        # 转换为整数类型
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        # 绘制矩形区域
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # 显示结果
        cv2.imshow("Image with Rectangle", image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_coordinate(self, element, coordinates):

        t = element["type"]
        if t == "letter":
            # 找到所有大写和小写字母
            coordinate_list = filter(lambda x: len(x["label_name"])==1 and x["label_name"].isalpha(), coordinates)
        elif t == "lowercase":
            coordinate_list = filter(lambda x: len(x["label_name"])==1 and x["label_name"].islower(), coordinates)
        elif t == "uppercase":
            coordinate_list = filter(lambda x: len(x["label_name"])==1 and x["label_name"].isupper(), coordinates)
        elif t == 'triangular' or t == 'triangular-prism':
            # 找到三角棱镜
            coordinate_list = filter(lambda x: x["label_name"] == 'triangular-prism', coordinates)

        elif t == 'geometry':
            # 找到几何图形
            label_list = [
                "column",
                "round_table",
                "octahedron",
                "polyhedron",
                "triangular-prism",
                "sphere",
                "cone"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)
        elif t == "number":
            # 找到所有数字
            coordinate_list = filter(lambda x: x["label_name"].isnumeric(), coordinates)
        elif t == "sphere":
            label_list = [
                "sphere"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)
        elif t == "cone":
            label_list = [
                "cone"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)
        elif t == "cylinder" or t == "column":
            label_list = [
                "column"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)

        elif t == "circular" or t == "round_table":
            # 截锥
            label_list = [
                "round_table"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)
        elif t == "cube":
            # 截锥
            label_list = [
                "cube"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)

        elif t == 'polyhedra' or t == 'polyhedron' or t == 'octahedron':
            label_list = [
                "octahedron", "polyhedron"
            ]
            coordinate_list = filter(lambda x: x["label_name"] in label_list, coordinates)
        elif t == "object":
            coordinate_list = coordinates
        else:
            return []
        res = list(coordinate_list)
        if element.get("value"):
            res = list(filter(lambda x: x["label_name"]==element.get("value"),res))
        if not res:
            raise ValueError("没有找到元素")
        if element.get("color"):
            res = list(filter(lambda coordinate: self.get_color(coordinate) == element["color"], res))
        if element.get("verb"):
            verb = element["verb"]
            if verb == 'once' or verb == 'single':
                coordinate_count = Counter(coordinate['label_name'] for coordinate in res)
                coordinate = list(filter(lambda x: x[1] == 1, coordinate_count.items()))
                if coordinate:
                    res = list(filter(lambda x: x['label_name'] == coordinate[0][0], res))
        return res

    def save_image(self,coordinate,name):
        nparr = np.frombuffer(self.image, np.uint8)
        # image = cv2.imread(self.image)
        image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)


        if coordinate.get("rotation"):
            rect = ((coordinate['box_mid_xy'][0], coordinate['box_mid_xy'][1]),
                    (coordinate["width"] - 7, coordinate["height"] - 7), coordinate["rotation_origin"])
            box = cv2.boxPoints(rect)
            box = np.intp(box)
            rect = cv2.minAreaRect(box)
            center, size, theta = rect

            x, y = center
            w, h = size
            if theta < -45:
                theta += 90

            # 使用 OpenCV 进行图像剪裁
            # img = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
            # img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            rows, cols = image.shape[:2]
            M = cv2.getRotationMatrix2D(center, theta, 1)
            img_rotated = cv2.warpAffine(image, M, (cols, rows))

            # 根据旋转后的矩形信息进行剪裁
            cropped_image = cv2.getRectSubPix(img_rotated, (int(w), int(h)), (x, y))

            # cv2.imshow(coordinate["label_name"], cropped_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        else:

            # 定义四个点坐标
            x1, y1, x2, y2 = coordinate["xyxy"]

            # 转换为整数类型
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cropped_image = image[y1:y2, x1:x2]
        cv2.imwrite(name, cropped_image)


    def get_color(self, coordinate):
        # 读取图片
        nparr = np.frombuffer(self.image, np.uint8)
        # image = cv2.imread(self.image)
        image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

        if coordinate.get("rotation"):
            rect = ((coordinate['box_mid_xy'][0] / 0.762, coordinate['box_mid_xy'][1]/ 0.762),
                    (coordinate["width"]/ 0.762-7, coordinate["height"]/ 0.762-7), coordinate["rotation_origin"])
            box = cv2.boxPoints(rect)
            box = np.intp(box)
            rect = cv2.minAreaRect(box)
            center, size, theta = rect

            x, y = center
            w, h = size
            if theta < -45:
                theta += 90

            # 使用 OpenCV 进行图像剪裁
            # img = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
            # img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            rows, cols = image.shape[:2]
            M = cv2.getRotationMatrix2D(center, theta, 1)
            img_rotated = cv2.warpAffine(image, M, (cols, rows))

            # 根据旋转后的矩形信息进行剪裁
            cropped_image = cv2.getRectSubPix(img_rotated, (int(w), int(h)), (x, y))

            # cv2.imshow(coordinate["label_name"], cropped_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        else:

            # 定义四个点坐标
            x1, y1, x2, y2 = coordinate["xyxy"]

            # 转换为整数类型
            x1, y1, x2, y2 = int(x1/ 0.762), int(y1/ 0.762), int(x2/ 0.762), int(y2/ 0.762)

            cropped_image = image[y1:y2, x1:x2]
        cv2.imwrite(self.tmp_img, cropped_image)

        color = get_color(self.tmp_img)
        os.remove(self.tmp_img)
        return color

    def get_volume(self, coordinate):
        if coordinate.get("width") and coordinate.get("height"):
            return coordinate.get("width") * coordinate.get("height")
        xyxy = coordinate["xyxy"]
        return (xyxy[2] - xyxy[0]) * (xyxy[3] - xyxy[1])

    def is_rota(self, coordinate):
        nparr = np.frombuffer(self.image, np.uint8)
        # image = cv2.imread(self.image)
        image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)


        if coordinate.get("rotation"):
            rect = ((coordinate['box_mid_xy'][0], coordinate['box_mid_xy'][1]),
                    (coordinate["width"] - 7, coordinate["height"] - 7), coordinate["rotation_origin"])
            box = cv2.boxPoints(rect)
            box = np.intp(box)
            rect = cv2.minAreaRect(box)
            center, size, theta = rect

            x, y = center
            w, h = size
            if theta < -45:
                theta += 90

            # 使用 OpenCV 进行图像剪裁
            # img = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
            # img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            rows, cols = image.shape[:2]
            M = cv2.getRotationMatrix2D(center, theta, 1)
            img_rotated = cv2.warpAffine(image, M, (cols, rows))

            # 根据旋转后的矩形信息进行剪裁
            cropped_image = cv2.getRectSubPix(img_rotated, (int(w), int(h)), (x, y))

            # cv2.imshow(coordinate["label_name"], cropped_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        else:

            # 定义四个点坐标
            x1, y1, x2, y2 = coordinate["xyxy"]

            # 转换为整数类型
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cropped_image = image[y1:y2, x1:x2]
        # cv2.imwrite(self.tmp_img, cropped_image)
        #
        # color = get_color(self.tmp_img)
        # print(color, coordinate["label_name"])
        # os.remove(self.tmp_img)

        return self.predict.is_rota(cropped_image)

        return
    def get_distance(self, xy, xy1):
        x1, y1 = xy
        x2, y2 = xy1
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def start(self, text=None):
        semantic = Semantic(text)
        text_obj = semantic.parse()

        coordinates = self.predict.predict()

        if text_obj.unique:
            # 寻找唯一的
            coordinate_count = Counter(coordinate['label_name'] for coordinate in coordinates)
            coordinate = list(filter(lambda x: x[1]==1, coordinate_count.items()))
            if coordinate:
                return list(filter(lambda x: x["label_name"]==coordinate[0][0], coordinates))
            else:
                raise ValueError("识别不准确")
        if text_obj.order:
            # 按照顺序点
            coordinate_list = []
            for i in text_obj.order:
                for c in coordinates:
                    if c["label_name"]==i:
                        coordinate_list.append(c)
            return coordinate_list
        if text_obj.transit:
            category = text_obj.transit["category"]
            # 寻找中间元素
            if category == "nearest" or category == "closest":
                transit_coordinate = self.get_coordinate(text_obj.transit, coordinates)

                if len(transit_coordinate) !=1:
                    raise ValueError(f"寻找最接近的目标出错,text:{text},")

                point_coordinate_list = self.get_coordinate(text_obj.point, coordinates)
                min_distance = 0
                min_point_coordinate = {}
                for point_coordinate in point_coordinate_list:
                    distance = self.get_distance(
                        transit_coordinate[0]["box_mid_xy"], point_coordinate["box_mid_xy"]
                    )
                    if min_distance == 0:
                        min_distance = distance
                        min_point_coordinate = point_coordinate
                    else:
                        if distance < min_distance:
                            min_distance = distance
                            min_point_coordinate = point_coordinate
                if not min_distance:
                    raise ValueError(f"没有最接近的元素, text:{text}")
                return [min_point_coordinate]
            elif category == "corresponding":
                transit_coordinates = self.get_coordinate(text_obj.transit, coordinates)

                if text_obj.point["type"] == "lowercase":
                    text_obj.point["value"] =transit_coordinates[0]["label_name"].lower()
                elif text_obj.point["type"] == "uppercase":
                    text_obj.point["value"] = transit_coordinates[0]["label_name"].upper()
                point_coordinates = self.get_coordinate(text_obj.point, coordinates)

                return point_coordinates
            elif category == "right" or category == "left" or category=='behind' or category=="in front":
                transit_coordinates = self.get_coordinate(text_obj.transit, coordinates)
                point_coordinates = self.get_coordinate(text_obj.point, coordinates)
                res = []
                if category == "right":
                    for point in point_coordinates:
                        if point["box_mid_xy"][0] > transit_coordinates[0]["box_mid_xy"][0]:
                            res.append(point)

                elif category == "left":
                    for point in point_coordinates:
                        if point["box_mid_xy"][0] < transit_coordinates[0]["box_mid_xy"][0]:
                            res.append(point)
                elif category == "behind":
                    for point in point_coordinates:
                        if point["box_mid_xy"][1] < transit_coordinates[0]["box_mid_xy"][0]:
                            res.append(point)
                elif category == "in front":
                    for point in point_coordinates:
                        if point["box_mid_xy"][1] > transit_coordinates[0]["box_mid_xy"][0]:
                            res.append(point)
                return res
            elif category == "above":
                transit_coordinates = self.get_coordinate(text_obj.transit, coordinates)
                point_coordinates = self.get_coordinate(text_obj.point, coordinates)

                min_distance = 0
                res_coordinates = {}
                for transit in transit_coordinates:
                    for point in point_coordinates:
                        # 首先判断x轴相差不大
                        if abs(point["box_mid_xy"][0] - transit["box_mid_xy"][0]) > 10:
                            continue
                        if point["box_mid_xy"][1] < transit["box_mid_xy"][1]:
                            distance = self.get_distance(transit["box_mid_xy"], point["box_mid_xy"])
                            if min_distance == 0 or distance < min_distance:
                                min_distance = distance
                                res_coordinates = point
                return [res_coordinates]
            elif category == "below":
                transit_coordinates = self.get_coordinate(text_obj.transit, coordinates)
                point_coordinates = self.get_coordinate(text_obj.point, coordinates)

                min_distance = 0
                res_coordinates = {}
                for transit in transit_coordinates:
                    for point in point_coordinates:
                        if abs(point["box_mid_xy"][0] - transit["box_mid_xy"][0]) > 10:
                            continue
                        if point["box_mid_xy"][1] > transit["box_mid_xy"][1]:
                            distance = self.get_distance(transit["box_mid_xy"], point["box_mid_xy"])
                            if min_distance == 0 or distance < min_distance:
                                min_distance = distance
                                res_coordinates = point
                return [res_coordinates]
            elif category == "same":
                transit_coordinates = self.get_coordinate(text_obj.transit, coordinates)

                if not transit_coordinates:
                    raise ValueError(f"没有找到相关元素")
                text_obj.point["type"] = transit_coordinates[0]["label_name"]
                coordinates = filter(lambda coordinate: coordinate['label_id'] != transit_coordinates[0]['label_id'], coordinates)
                point_coordinates = self.get_coordinate(text_obj.point, coordinates)
                return point_coordinates

        if text_obj.point:

            if text_obj.point.get("category"):
                if "all " in text_obj.point["category"]:
                    all_type = text_obj.point["category"].split()[-1]
                    point_coordinates = self.get_coordinate(text_obj.point, coordinates)

                    if all_type == 'duplicate':
                        point_coordinates_count = Counter(coordinate['label_name'] for coordinate in coordinates)

                        for label_name,count in point_coordinates_count.items():
                            if count>1:
                                point_coordinates = filter(lambda coordinate: coordinate['label_name'] == label_name, point_coordinates)
                                return list(point_coordinates)
                    elif all_type == "tilted":
                        point_coordinates = self.get_coordinate(text_obj.point, coordinates)
                        return list(filter(lambda x:15<abs(x["rotation"])<80,point_coordinates))
                    elif all_type == "larger":
                        point_coordinates = self.get_coordinate(text_obj.point, coordinates)

                        return list(filter(lambda point:self.get_volume(point)>800,point_coordinates))
                    elif all_type == "smaller":
                        point_coordinates = self.get_coordinate(text_obj.point, coordinates)
                        return list(filter(lambda point: self.get_volume(point) < 800, point_coordinates))

                elif text_obj.point["category"]=="smaller" or text_obj.point["category"]=="larger":
                    point_coordinates = self.get_coordinate(text_obj.point, coordinates)

                    if not point_coordinates:
                        raise ValueError(f"没有找到相关颜色元素")
                    volume = 0
                    point_coordinate = {}
                    for point in point_coordinates:
                        v = self.get_volume(point)
                        if text_obj.point["category"] == "smaller":
                            if volume == 0:
                                volume = v
                                point_coordinate = point
                            else:
                                if v < volume:
                                    volume = v
                                    point_coordinate = point
                        elif text_obj.point["category"] == "larger":
                            if volume == 0:
                                volume = v
                                point_coordinate = point
                            else:
                                if v > volume:
                                    volume = v
                                    point_coordinate = point
                    return [point_coordinate]

                elif text_obj.point["category"] == "unrotated" or text_obj.point["category"] == "rotated":
                    res = []
                    point_point_coordinates = self.get_coordinate(text_obj.point, coordinates)
                    for c in point_point_coordinates:
                        if self.is_rota(c) == text_obj.point["category"]:
                            res.append(c)
                    return res

            else:
                point_coordinates = self.get_coordinate(text_obj.point, coordinates)


                if point_coordinates:
                    return [point_coordinates[0]]
        raise ValueError(f"没有找到相关元素")


if __name__ == "__main__":

    import os

    with open(r"5.png", 'rb') as r:
        img = r.read()
    itt = Identity(img)
    res = itt.start(text="1713035104_Please_click_on_the_letter_above_cube".replace("_", ' '), )
    print(res)


    #     itt.draw_image(i)
    # import json
    # print(json.dumps(res,indent=4))

