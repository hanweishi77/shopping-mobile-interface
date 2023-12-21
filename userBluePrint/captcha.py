from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from string import digits, ascii_letters


# 单例
def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton_wrapper


# 获取验证码
@Singleton
class GenerateCaptcha:
    def __init__(self):
        pass

    # 生成验证码背景图片
    def _generate_image(self, width=120, height=40, color=(255, 255, 255)):
        # 创建一个Image对象，设置图片的大小和背景颜色 mode, size, color
        img = Image.new('RGB', (width, height), color)
        # 返回Image对象
        return img

    # 给图片对象添加验证码字符
    def _add_captcha(self, img, font_style='arial.ttf', font_size=25, length=4):
        # 创建一个Draw对象
        draw = ImageDraw.Draw(img)
        # 定义验证码字符集A-Za-z0-9
        captcha_chars = digits + ascii_letters
        # 随机生成4个字符作为验证码内容
        captcha_chars_my = ''.join(random.sample(captcha_chars, length))
        # 设置字体
        font = ImageFont.truetype(font_style, font_size)
        # 计算文本位置
        text_x = 10
        text_y = 10
        # 为每个字符设置一个随机的颜色
        for i in range(4):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.text((text_x, text_y), captcha_chars_my[i], font=font, fill=color)
            text_x += 20
        # 返回验证码字符
        return captcha_chars_my

    # 添加验证码干扰元素
    def _add_interference(self, img):
        # 创建一个Draw对象
        draw = ImageDraw.Draw(img)
        # 随机生成干扰元素
        for i in range(150):
            x = random.randint(0, 120)
            y = random.randint(0, 40)
            draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # 对验证码图片进行处理
    def _process_image(self, img):
        # 定义一个BlurFilter对象
        blur_filter = ImageFilter.BLUR
        # 对图片进行模糊处理
        img = img.filter(blur_filter)
        # 返回处理过的Image对象
        return img

    def get_captcha(self):
        # 生成验证码图片
        image = self._generate_image()
        # 添加验证码内容
        captcha4 = self._add_captcha(image)
        # 添加干扰元素
        self._add_interference(image)
        # 对验证码图片进行处理
        # image = self._process_image(image)
        # 保存验证码图片
        image.save('./static/tmp/captcha.png')
        # 返回验证码
        return captcha4


captcha = GenerateCaptcha()
print(captcha.get_captcha())
# captcha1 = GenerateCaptcha()
# print(captcha1.get_captcha())
# print(captcha is captcha1)
