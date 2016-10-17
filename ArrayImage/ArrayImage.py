import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

class TextImage():

    def __init__(self, texts):
        self.texts = texts
        self.fontname = '/Library/Fonts/Times New Roman.ttf'
        self.occupancy = 1.0
        self.center = True

    def __call__(self, image, x1, y1, x2, y2):
        if not os.path.exists(self.fontname):
            print('Fontname {} is not exist'.format(self.fontname))

        length = len(self.texts)
        textheight = (y2 - y1)/length
        img = Image.new('RGBA', (x2-x1, y2-y1), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.fontname, int(textheight*self.occupancy))
        #make image with texts
        for i, text in enumerate(self.texts):
            draw.text((0, textheight*i), text, font=font, fill='#000')
        centerize = 0.5 if self.center else 1
        image.paste(img, (x1, y1 + int(textheight*(1-self.occupancy)*centerize)), img)

        return image

    def settings(self, fontname='/Library/Fonts/Times New Roman.ttf', occupancy=1.0, center=True):
        self.fontname=fontname
        self.occupancy = occupancy
        self.center = center

