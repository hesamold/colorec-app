from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import Rectangle
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

import io
from PIL import Image as PILImage


class ColorPickerApp(App):
    def build(self):
        self.image = None
        self.color_info_label = Label(text="RGB: (0, 0, 0)\nHex: #000000", color=(1, 1, 1, 1))
        
        self.layout = BoxLayout(orientation='vertical')
        
        self.image_widget = Image()
        self.layout.add_widget(self.image_widget)
        
        self.button_layout = BoxLayout(size_hint_y=0.1)
        
        upload_button = Button(text="Upload Image", on_press=self.upload_image)
        self.button_layout.add_widget(upload_button)
        
        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.color_info_label)
        
        self.image_widget.bind(on_touch_down=self.get_color_at_click)
        
        return self.layout

    def upload_image(self, instance):
        filechooser = FileChooserIconView()
        filechooser.bind(on_selection=lambda *x: self.load_image(filechooser.selection))
        
        popup = Popup(title="Select Image", content=filechooser, size_hint=(None, None), size=(400, 400))
        popup.open()

    def load_image(self, selection):
        if selection:
            image_path = selection[0]
            image = PILImage.open(image_path)
            image.save("temp_image.png")
            self.image_widget.source = "temp_image.png"
            self.image_widget.reload()

    def get_color_at_click(self, instance, touch):
        if self.image_widget.collide_point(touch.x, touch.y):
            image_data = self.image_widget.texture.pixels
            width = self.image_widget.texture.width
            height = self.image_widget.texture.height

            x = int(touch.x)
            y = int(touch.y)
            
            # Ensure x and y are within bounds
            if x < width and y < height:
                pixel_index = (y * width + x) * 4
                pixel = image_data[pixel_index:pixel_index+4]
                
                r, g, b, _ = pixel
                rgb = f"RGB: ({r}, {g}, {b})"
                hex_color = f"Hex: #{r:02x}{g:02x}{b:02x}".upper()
                
                self.color_info_label.text = f"{rgb}\n{hex_color}"
                
                # Change background color (this can be enhanced to show the color in the app UI)
                self.color_info_label.color = (r / 255, g / 255, b / 255, 1)


if __name__ == "__main__":
    ColorPickerApp().run()
