from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
Window.clearcolor = (0.1, 0.1, 0.1, 1)
class DonPlayer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)
        self.add_widget(Label(text='[b]DON PLAYER[/b]', markup=True, font_size=45, color=(1,0.8,0,1), size_hint=(1,0.7)))
        self.add_widget(Label(text='Mukodik a GitHub build!', font_size=22, color=(1,1,1,1), size_hint=(1,0.1)))
        btn = Button(text='LEJATSZAS', font_size=28, background_color=(1,0.8,0,1), size_hint=(1,0.2))
        btn.bind(on_press=self.play)
        self.add_widget(btn)
        self.lbl = Label(text='', font_size=18)
        self.add_widget(self.lbl)
    def play(self, x):
        self.lbl.text = "KESZ AZ APK!"
class DonApp(App):
    def build(self):
        return DonPlayer()
DonApp().run()
