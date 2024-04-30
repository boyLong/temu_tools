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
    r  = 1 / (1 + mse)
    return r


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


def pd_captcha(image_path):

    img_info = {}
    for index,img in enumerate(split_image_to_6(image_path, 2, 3)):

        img_info[index] = {
            "left": split_margin(img, 'left', 1),
            "top": split_margin(img, 'top', 1),
            "right": split_margin(img, 'right', 1),
            "bottom": split_margin(img, 'bottom', 1),
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
            if cur_socre > socre:
                cur_img_info = new_img_info
                socre = cur_socre
                point = [x,y]
    return point
    print(point)
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
if __name__ == '__main__':
    import base64
    import io
    img = base64.b64decode('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')
    image_stream = io.BytesIO(img)
    r = pd_captcha(image_stream)
