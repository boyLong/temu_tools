from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity
from copy import deepcopy

def split_image_to_6(image_path, rows, cols):
    # 打开图像
    img = Image.open(image_path)

    # 获取图像的宽度和高度
    width, height = img.size

    # 计算每个小图的宽度和高度
    small_width = width // cols
    small_height = height // rows

    # 切割图像并保存为小图
    img_list = []
    for row in range(rows):
        for col in range(cols):
            # 计算每个小图的左上角坐标和右下角坐标
            left = col * small_width
            top = row * small_height
            right = left + small_width
            bottom = top + small_height

            # 切割图像
            small_img = img.crop((left, top, right, bottom))
            img_list.append(small_img)

    return img_list


def split_margin(img, direction, margin):

    # 获取图像的宽度和高度
    width, height = img.size

    # 计算切割位置
    if direction == 'left':
        # 切割左侧
        left_img = img.crop((0, 0, margin, height))
        return  left_img
    elif direction == 'right':
        # 切割右侧
        right_img = img.crop((width - margin, 0, width, height))
        return right_img
    elif direction == 'top':
        # 切割顶部
        top_img = img.crop((0, 0, width, margin))
        return top_img
    elif direction == 'bottom':
        # 切割底部
        bottom_img = img.crop((0, height - margin, width, height))
        return bottom_img
    else:
        print("Invalid direction!")
        return None




def calculate_similarity(img1, img2):
    # 转换图像为灰度图
    img1_gray = img1.convert('RGBA')
    img2_gray = img2.convert('RGBA')
    # 转换图像为数组
    img1_array = np.array(img1_gray)
    img2_array = np.array(img2_gray)

    # 计算均方误差（MSE）
    mse = np.mean((img1_array - img2_array) ** 2)
    return  1 / (1 + mse)


def similar(img_info):

    score = 0
    # 计算图片1和他相邻的两个边框相似度，即0-1，0-3
    score += calculate_similarity(img_info[0]["right"], img_info[1]["left"])
    score += calculate_similarity(img_info[0]["bottom"], img_info[3]["top"])
    # 计算图片2和他相邻的两个边框相似度，即1-2，1-4
    score += calculate_similarity(img_info[1]["right"], img_info[2]["left"])
    score += calculate_similarity(img_info[1]["bottom"], img_info[4]["top"])
    #  计算图片3和他相邻的边框相似度，即2-5
    score += calculate_similarity(img_info[2]["bottom"], img_info[5]["top"])

    # 计算图片4和他相邻的边框相似度，即3-4
    score += calculate_similarity(img_info[3]["right"], img_info[4]["left"])

    # 计算图片5和他相邻的边框相似度，即4-5

    score += calculate_similarity(img_info[4]["right"], img_info[5]["left"])

    return score



img_info = {}
for index,img in enumerate(split_image_to_6('2.png', 2, 3)):
    img_info[index] = {
        "left": split_margin(img, 'left', 3),
        "top": split_margin(img, 'top', 3),
        "right": split_margin(img, 'right', 3),
        "bottom": split_margin(img, 'bottom', 3),
        "base": img
    }


socre = 0

point = []
cur_img_info = {}
for x in range(6):
    for y in range(x+1,6):
        new_img_info = deepcopy(img_info)
        new_img_info[x] = img_info[y]
        new_img_info[y] = img_info[x]
        cur_socre = similar(new_img_info)
        print(cur_socre,x,y)
        if cur_socre > socre:
            cur_img_info = new_img_info
            socre = cur_socre
            point = [x,y]
print(cur_img_info)
print(socre,point)
print(cur_img_info[0])
new_img = Image.new('RGBA', (cur_img_info[0]["base"].width * 3, cur_img_info[0]["base"].height * 2))

# 将小图像组装成新的图像
index = 0
for row in range(2):
    for col in range(3):
        new_img.paste(cur_img_info[index]["base"], (col * cur_img_info[0]["base"].width, row * cur_img_info[0]["base"].height))
        index += 1

new_img.show()