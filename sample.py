from ArrayImage.ArrayImage import TextImage
from PIL import Image

def main():
    texts = ['text{}'.format(i) for i in range(12)]
    image = Image.open('sample.png')

    textimg = TextImage(texts)
    textimg.settings(occupancy=0.6, center=True)
    image = textimg(image, 220, 200, 800, 800)
    image.save('output.png')

if __name__ == '__main__':
    main()
