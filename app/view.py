import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
#from view.home import UnaScreen
from controller.material import colors, fonts
class MainWid(ScreenManager):
    pass
    
  
class MainApp(App):
    title = "Screen Manager"
    colors = colors
    fonts = fonts
    def build(self):
        return MainWid()
