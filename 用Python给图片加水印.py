#学习给图片加水印的方法
#主要使用python第三方库PIL
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
def Num(filepath):
    img = Image.open(r'c:\test3.jpg') # 打开图片
    
    size = img.size
    # 获取图片尺寸（尺寸储存在一个tuple中）
    fontSize = int(size[1] / 4) 
    
    # 设置字体（fontsize）大小
    draw = ImageDraw.Draw(img) 
    #创建一个Draw对象
    
    ttFont = ImageFont.truetype("c:\windows\fonts\simsunb.ttf", fontSize)
    draw.text((size[0] - fontSize, 0), '3', (256, 0, 0), font = ttFont)
    
    del draw
    img.save('./result.jpg')
    img.show()
Num(r'c:\test3.jpg')
