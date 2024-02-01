
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from string import digits, ascii_letters
from io import BytesIO
import base64


# 单例
def Singleton(cls):
    instance = {}

    def _singleton_wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton_wrapper


# 获取验证码图片流，验证码
@Singleton
class GenerateCaptcha:
    """
        生成图片验证码
    """
    def __init__(self, width=120, height=40):
        self.width = width
        self.height = height
        self.img = Image.new('RGB', (width, height), (255, 255, 255))
        self.font = ImageFont.truetype('arial.ttf', size=25)
        self.draw = ImageDraw.Draw(self.img)

    def rand_color(self):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color

    def rand_code(self):
        # 定义验证码字符集A-Za-z0-9
        captcha_chars = digits + ascii_letters
        # 随机生成4个字符作为验证码内容
        code = ''.join(random.sample(captcha_chars, 4))
        return code

    def draw_lines(self, num=3):
        for num in range(num):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            self.draw.line(((x1, y1), (x2, y2)), fill=self.rand_color(), width=1)

    # 添加验证码干扰元素
    def draw_interference(self, num):
        # 随机生成干扰元素
        for i in range(num):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # 对验证码图片进行处理
    def process_image(self):
        # 定义一个BlurFilter对象
        blur_filter = ImageFilter.BLUR
        # 对图片进行模糊处理
        img = self.img.filter(blur_filter)
        # 返回处理过的Image对象
        return img

    # 生成验证码背景图片
    def draw_verify_image(self):
        # 随机字符
        code = self.rand_code()
        # 计算文本位置
        text_x = 10
        text_y = 10
        # 图层添加字符
        for _ in range(4):
            self.draw.text((text_x, text_y), text=code[_], font=self.font, fill=self.rand_color())
            text_x += 20
        # 干扰线
        self.draw_lines(2)
        # 干扰点
        self.draw_interference(150)
        # 保存本地,仅仅测试用！！！！！
        # self.img.save('./static/tmp/captcha.png')
        # self.img.show()
        buffered = BytesIO()
        # 保存到内存
        self.img.save(buffered, format='JPEG')
        # 字节流，便于img的src标签识别
        img_byt = b"data:image/png;base64," + base64.b64encode(buffered.getvalue())
        return img_byt, code


if __name__ == '__main__':
    captcha = GenerateCaptcha()
    print(captcha.draw_verify_image())
    # captcha1 = GenerateCaptcha()
    # print(captcha1.draw_verify_image())
    # print(captcha is captcha1)
