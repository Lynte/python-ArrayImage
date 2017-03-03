from ArrayImage.ArrayImage import TextImage
from PIL import Image


def main():
    texts = ['text{}'.format(i) for i in range(10)]
    texts += ['oaheuthatoenuhntaeouheteohauthteoatehaoutnhutenoahtnseahouhaoeuhtnhut']*2
    image = Image.open('sample.png')

    textimg = TextImage(occupancy=0.6)
    image = textimg(image, texts, 220, 200, 800, 800)
    image.save('output.png')

if __name__ == '__main__':
    main()
