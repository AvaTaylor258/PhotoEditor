import random

import ImageDraw
from PIL.Image import Image
from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image

class PhotoEditorApp(App):
    pass

class Editor(Screen):
    def change_image(self, t):
        self.ids.image_display.source = f"user_images/{t}"

    def black_and_white(self, t):
        img = Image.open(t)
        pixels = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                red = pixels[x, y][0]  # val stored for red color channel
                green = pixels[x, y][1]  # val stored for green color channel
                blue = pixels[x, y][2]  # val stored for blue color channel
                avg = int((red + green + blue) / 3)

                pixels[x, y] = (avg, avg, avg)  # assigns the pixel a new tuple made up of avg of the RGB
        new_name = f"{t[0:-4]}_blck_wht.png"
        img.save(new_name)
        self.ids.image_display.source = new_name

    def inverse(self, t): # work on!!!
        img = Image.open(t)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 225 - pixels[x, y][0]
                green = 225 - pixels[x, y][1]
                blue = 225 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        new_name = f"{t[0:-4]}_inversed.png"
        img.save(new_name)
        self.ids.image_display.source = new_name

    def line_drawing(self, t):
        leeway = 150  # how far apart the vals can be (used to be 113 bc half-ish of 225)
        img = Image.open(t)
        pixels = img.load()
        for y in range(0, img.size[1]):
            for x in range(0, img.size[0] - 1, 2):
                red1 = pixels[x, y][0]
                green1 = pixels[x, y][1]
                blue1 = pixels[x, y][2]

                red2 = pixels[x + 1, y][0]
                green2 = pixels[x + 1, y][1]
                blue2 = pixels[x + 1, y][2]

                pixel1 = red1 + green1 + blue1
                pixel2 = red2 + green2 + blue2
                avg1 = pixel1 / 3
                avg2 = pixel2 / 3
                if abs(avg1 - avg2) > leeway and avg1 > avg2:
                    pixels[x, y] = (0, 0, 0)
                    pixels[x + 1, y] = (225, 225, 225)
                elif abs(avg1 - avg2) > leeway and avg1 < avg2:
                    pixels[x, y] = (225, 225, 225)
                    pixels[x + 1, y] = (0, 0, 0)
                elif ((avg1 + avg2) / 2) > leeway:
                    pixels[x, y] = (225, 225, 225)
                    pixels[x + 1, y] = (225, 225, 225)
                elif ((avg1 + avg2) / 2) < leeway:
                    pixels[x, y] = (0, 0, 0)
                    pixels[x + 1, y] = (0, 0, 0)
        new_name = f"{t[0:-4]}_lined.png"
        img.save(new_name)
        self.ids.image_display.source = new_name

    def pointillism(self, t):
        img = Image.open(t)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")
        for i in range(500000):
            x = random.randint(0, img.size[0] - 1)
            y = random.randint(0, img.size[1] - 1)
            size = random.randint(10, 15)
            ellipse_box = [(x, y), (x + size, y + size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipse_box, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))
            del draw
        new_name = f"{t[0:-4]}_pointed.png"
        canvas.save(new_name)
        self.ids.image_display.source = new_name

    def sepia(self, t):
        img = Image.open(t)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red_og = pixels[x, y][0]
                green_og = pixels[x, y][1]
                blue_og = pixels[x, y][2]
                red = int(red_og * .393 + green_og * .769 + blue_og * .189)
                green = int(red_og * .349 + green_og * .686 + blue_og * .168)
                blue = int(red_og * .272 + green_og * .534 + blue_og * .131)
                pixels[x, y] = (red, green, blue)
        new_name = f"{t[0:-4]}_sepia.png"
        img.save(new_name)
        self.ids.image_display.source = new_name

    def pixelate(self, t, x, y, width, height): # doesn't work - teach said he would run thru it w/ us
        skip = 15
        img = Image.open(t)
        pixels = img.load()
        for yy in range(y, y + height, skip):
            for xx in range(x, x + width, skip):
                temp = pixels[xx, yy]
                for i in range(yy, yy + skip):
                    for j in range(xx, xx + skip):
                        pixels[j, i] = temp
        new_name = f"{t[0:-4]}_pixelated.png"
        img.save(new_name)
        self.ids.image_display.source = new_name

PhotoEditorApp().run()