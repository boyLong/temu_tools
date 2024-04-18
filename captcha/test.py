from ultralytics import YOLO
from cpuinfo import cpuinfo

print(cpuinfo.get_cpu_info())
model = YOLO(r'.\bt\1.onnx')
results = model(r'1.png', save=True)


# def get_coordinate(results):
#     coordinates = []
#     for result in results:
#         names = result.names
#
#         data = result.obb.data
#         tabs = []
#         for tab in data:
#             x_center, y_center, width, height, rotation,score, cls_id = tab
#             cls_name = names[cls_id.item()]
#             rotation = rotation.item()
#             tabs.append([x_center.item(), y_center.item(), width.item(), height.item(), rotation,int(rotation * 180/3.1415-90), score.item(), cls_name])
#         coordinates.append(tabs)
#     return coordinates
#
# coordinates = get_coordinate(results)
# for coord in coordinates[0]:
#     print(coord)
