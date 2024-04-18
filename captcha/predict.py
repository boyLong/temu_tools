# --coding: utf-8 --
import json
import os
from ultralytics import YOLO
from PIL import Image
import io

model_path = os.path.dirname(__file__)
model_cls = YOLO(os.path.join(model_path, "bt", "class.pt"))
model_0 = YOLO(os.path.join(model_path, "bt", r"0.pt"))
model_1 = YOLO(os.path.join(model_path, "bt", r"1.onnx"), task="detect")
model_rota = YOLO(os.path.join(model_path, "bt", r"rota.pt"), task="detect")

class Predict(object):
    def __init__(self, img, model_cls=1):
        self.img = self.read_img(img)

        if model_cls is None:
            self.model_cls = self.get_img_model()
        else:
            self.model_cls = model_cls
    @staticmethod
    def read_img(img):
        image_stream = io.BytesIO()
        image_stream.write(img)
        image_stream.seek(0)
        return Image.open(image_stream)

    def get_img_model(self):
        d = model_cls(self.img)
        return d[0].probs.top1
    def is_rota(self, image):
        d = model_rota(image)
        return d[0].names[d[0].probs.top1]
    def predict(self):
        if int(self.model_cls) == 0:
            results= model_0.predict(self.img)
            return self.get_result(results[0])
        elif int(self.model_cls) == 1:
            results = model_1.predict(self.img)
            return self.get_result_2(results[0])
        else:
            raise TypeError("Unknown model type")

    def get_result(self,result):

        names = result.names

        data = result.obb.data
        tabs = []
        for tab in data:
            x_center, y_center, width, height, rotation, score, cls_id = tab.tolist()

            # rect = ((x_center, y_center), (width, height), rotation)
            # box = cv2.boxPoints(rect)
            # box = np.int0(box)
            # rect = cv2.minAreaRect(box)
            # center, size, theta = rect
            #
            # x, y = center
            # w, h = size
            # if theta < -45:
            #     theta += 90
            #
            # # 使用 OpenCV 进行图像剪裁
            # img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
            #
            # rows, cols = img.shape[:2]
            # M = cv2.getRotationMatrix2D(center, theta, 1)
            # img_rotated = cv2.warpAffine(img, M, (cols, rows))
            #
            # # 根据旋转后的矩形信息进行剪裁
            # img_cropped = cv2.getRectSubPix(img_rotated, (int(w), int(h)), (x, y))

            # cv2.imshow('Cropped Image', img_cropped)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            cls_name = names[cls_id]
            tabs.append({
                "label_id": int(cls_id),
                "label_name": cls_name,
                "box_mid_xy": [x_center, y_center],
                "rotation": int(rotation * 180 / 3.1415 - 90),
                "rotation_origin": rotation,
                "width": width,
                "height": height
            })

        return tabs
    def get_result_2(self,result):
        cls_xy = list()
        cls_dict = result.names
        cls_all = result.boxes.cls.tolist()
        xyxy_all = result.boxes.xyxy.tolist()
        for i in range(len(cls_all)):
            label_name = cls_dict[int(cls_all[i])]
            box_xyxy = xyxy_all[i]
            box_mid_xy = [(box_xyxy[0] + box_xyxy[2]) / 2, (box_xyxy[1] + box_xyxy[3]) / 2]

            box_mid_xy = [box_mid_xy[0] * 0.762, box_mid_xy[1] * 0.762]
            box_xyxy = [box_xyxy[0] * 0.762, box_xyxy[1] * 0.762,box_xyxy[2] * 0.762,box_xyxy[3] * 0.762]
            cls_xy.append({
                "label_id": i,
                "label_name": label_name,
                "box_mid_xy": box_mid_xy, "xyxy": box_xyxy,
                "rotation": 0,
            })
        return cls_xy


if __name__ == '__main__':
    # img_path = r"C:\Users\13106\Documents\WeChat Files\wxid_ju84rt2s2z1w22\FileStorage\File\2024-02\work\work\yolo_work\temu\dataset\train\images\211.png"
    img_path = r"D:\dev\databurning\temu_new\1.png"
    with open(img_path, "rb") as f:
        img = f.read()
    ity = Predict(img)

    print(json.dumps(ity.predict(), indent=1))

    print(ity.model_cls)