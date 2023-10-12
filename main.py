from kivy.app import App
from kivy.uix.screenmanager import Screen
# unable to install PIL due to IDE/C: error (c. very stupid and frustrating pip)

class PhotoEditorApp(App):
    pass

class Editor(Screen):
    def change_image(self, t):
        print(t)
        self.ids.image_display.source = f"user_images/{t}"
    def black_and_white(self, t, red_val, green_val, blue_val):
        img = Image.open(t)

PhotoEditorApp().run()