import os
from datetime import datetime


class Rename(object):
    def __init__(self, path=r'C:/Users/22762/Desktop/dd/category'):
        self.path = path

    def rename(self):
        filelist = os.listdir(self.path)  # 目录下的文件夹或文件名列表
        i = 1
        for item in filelist:
            if '.' in item and item.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif']:
                src = os.path.join(os.path.abspath(self.path), item)
                file_end = os.path.splitext(item)[-1]
                dst = os.path.join(os.path.abspath(self.path), datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(i) + file_end)
                try:
                    os.rename(src, dst)
                    print('converting%s%s...' % (src, dst))
                    i = i+1
                except Exception as e:
                    print('错误信息：', e)
                    continue


if __name__ == '__main__':
    demo = Rename()
    demo.rename()
