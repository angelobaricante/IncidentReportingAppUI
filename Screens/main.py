from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 600)

class MyApp(MDApp):
    def build(self):
        screen_manager = MDScreenManager()
        screen_manager.add_widget(Builder.load_file("Screens\LoginScreen\main.kv"))
        screen_manager.add_widget(Builder.load_file("Screens\HomeScreen\screenreport.kv"))
        screen_manager.add_widget(Builder.load_file("Screens\HomeScreen\homescreen.kv"))
        screen_manager.add_widget(Builder.load_file("Screens\LoginScreen\login.kv"))
        screen_manager.add_widget(Builder.load_file("Screens\LoginScreen\signup.kv"))
        screen_manager.add_widget(Builder.load_file("Screens\HomeScreen\sosscreen.kv"))
        screen_manager.add_widget(Builder.load_file("Screens\HomeScreen\homescreen_admin.kv"))
        return screen_manager

if __name__ == "__main__":
    LabelBase.register(name = "MPoppins", fn_regular="C:\\Fonts\\Poppins\\Poppins-Medium.ttf")
    LabelBase.register(name = "BPoppins", fn_regular="C:\\Fonts\\Poppins\\Poppins-SemiBold.ttf")

    MyApp().run()