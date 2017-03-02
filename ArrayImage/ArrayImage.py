import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os


class TextImage():

    def __init__(self, font='/Library/Fonts/Times New Roman.ttf',
                 occupancy=1.0, iscenter=True):
        self.fontname = font
        self.occupancy = occupancy
        self.center = iscenter

    def __call__(self, image, texts, x1, y1, x2, y2):
        if not os.path.exists(self.fontname):
            print('Fontname {} is not exist'.format(self.fontname))

        length = len(texts)
        textheight = (y2 - y1) / length
        img = Image.new('RGBA', (x2 - x1, y2 - y1), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(
            self.fontname, int(textheight * self.occupancy), encoding='unic')

        # make image with texts
        for i, text in enumerate(texts):
            sfont = font
            textsize = font.getsize(text)
            if textsize[0] > (x2-x1) :
                fontscale = (x2-x1) / textsize[0]
                sfont = ImageFont.truetype(self.fontname, int(textheight * self.occupancy * fontscale), encoding='unic')
            draw.text((0, textheight * i), text, font=sfont, fill='#000')

        centerize = 0.5 if self.center else 1
        pastedimage = image.copy()
        pastedimage.paste(
            img, (x1, y1 + int(textheight * (1 - self.occupancy) * centerize)), img)

        return pastedimage
