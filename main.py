
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

class BoxLayoutExample(BoxLayout):
    pass

# Κλάση που κληρονομεί από App και είναι η εφαρμογή μας
class TheLabApp(App):
    pass

# Κλάση Widget, δηλαδή το κύριο widget της εφαρμογής μας
class MainWidget(Widget):
    pass

class AnchorExampleLayout(AnchorLayout):
    pass

class GridLayoutExample(GridLayout):
    pass
class StackLayoutExample(StackLayout):
    pass
class ScrollViewExample(ScrollView):
    pass
class WidgetsExample(GridLayout):
    my_text=StringProperty("hello!!!")
    my_score = StringProperty("1")
    score=1
    def on_button_click(self):
        print("button clicked")
        self.my_text="you clicked me"
    def scoring(self):
        self.score+=1
        self.my_score=str(self.score)
    def on_toggle_button(self,widget,Button):
        if widget.state=="normal":
            widget.text="off"
            Button.text=0

        else:
            widget.text="on"
TheLabApp().run()

        

