import random

import ImageDraw
from PIL.Image import Image
from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image
# unable to install PIL due to IDE/C: error (c. very stupid and frustrating pip)

class PhotoEditorApp(App):
    pass

class Editor(Screen):
    def change_image(self, t):
        self.ids.image_display.source = f"user_images/{t}"

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

PhotoEditorApp().run()