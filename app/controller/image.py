#!encoding=utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def image_tran(img_src,filename):
    image = Image.open(img_src)#new('RGB', (width, height), (255, 255, 255))
    image = image.filter(ImageFilter.CONTOUR)
    image.save("/flask/gx/app/static/images/"+filename)


