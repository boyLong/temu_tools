import colorsys
import PIL.Image as Image


# 获取图片主要颜色rgb值
def get_dominant_color(image):
    max_score = 0.0001
    dominant_color = None
    for count, (r, g, b) in image.getcolors(image.size[0] * image.size[1]):
        # 转为HSV标准
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        if y > 0.9:
            continue
        score = (saturation + 0.1) * count
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color


# 图片rgb值转为hsv
def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g - b) / m) * 60
        else:
            h = ((g - b) / m) * 60 + 360
    elif mx == g:
        h = ((b - r) / m) * 60 + 120
    elif mx == b:
        h = ((r - g) / m) * 60 + 240
    if mx == 0:
        s = 0
    else:
        s = m / mx
    v = mx

    # 此时h,s,v值范围分别是0-360, 0-1, 0-1，在OpenCV中，H,S,V范围是0-180,0-255,0-255，加上下面代码转换：
    H = h / 2
    S = s * 255.0
    V = v * 255.0

    return H, S, V


# # 返回值是255 100 100的范围
#     return h,s*100,v*100


def pan_duan_yan_se(h_0, s_0, v_0):
    if 0 <= h_0 < 180 and 0 <= s_0 < 255 and 0 <= v_0 < 46:
        return "黑色"
    elif 0 <= h_0 < 180 and 0 <= s_0 < 43 and 46 <= v_0 < 220:
        return "gray"
    elif 0 <= h_0 < 180 and 0 <= s_0 < 30 and 221 <= v_0 < 255:
        print("白色")
        return "白色"
    elif (0 <= h_0 < 10 or 156 <= h_0 < 180) and 43 <= s_0 < 255 and 46 <= v_0 < 255:
        return "red"
    elif 11 <= h_0 < 25 and 43 <= s_0 < 255 and 16 <= v_0 < 255:
        return "yellow"
    elif 26 <= h_0 < 34 and 43 <= s_0 < 255 and 46 <= v_0 < 255:
        return "yellow"
    elif 35 <= h_0 < 77 and 43 <= s_0 < 255 and 46 <= v_0 < 255:
        return "green"
    elif 78 <= h_0 < 99 and 43 <= s_0 < 255 and 46 <= v_0 < 255:
        return "green"
    elif 100 <= h_0 < 124 and 43 <= s_0 < 255 and 46 <= v_0 < 255:

        return "blue"
    elif 125 <= h_0 < 155 and 43 <= s_0 < 255 and 46 <= v_0 < 255:
        return "blue"
    else:
        print("色调H超出范围，饱和度S，亮度V明度")
        return "blue"


def get_color(image):
    image = Image.open(image)
    image = image.convert("RGB")
    r, g, b = (
        get_dominant_color(image)[0],
        get_dominant_color(image)[1],
        get_dominant_color(image)[2],
    )
    hsv_value = rgb2hsv(r, g, b)
    h_0 = hsv_value[0]
    s_0 = hsv_value[1]
    v_0 = hsv_value[2]
    return pan_duan_yan_se(h_0, s_0, v_0)
if __name__ == '__main__':
    print(get_color("7ff70ace-dd92-4b75-bbd7-35b91790e622.jpg"))