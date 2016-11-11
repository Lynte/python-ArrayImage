import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

class TextImage():

    def __init__(self, texts, font='/Library/Fonts/Times New Roman.ttf', 
            occupancy=1.0, iscenter=True):
        self.texts = texts
        self.fontname = font
        self.occupancy = occupancy
        self.center = iscenter

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
        pastedimage = image.copy()
        pastedimage.paste(img, (x1,
            y1 + int(textheight*(1-self.occupancy)*centerize)), img)

        return pastedimage
