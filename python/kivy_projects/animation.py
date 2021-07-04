from kivy import app
from kivy import animation
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder   
from kivy.animation import Animation
from kivy.core.window import Window

Window.size = (800,600)

Builder.load_file("animation.kv")

class MyLayout(Widget):
    def moove_it(self, widget, *args):
        animate = Animation( 
            background_color = (0.5, 0.5, 0.5, 0.5) 
            , duration = 3
            , opacity = 0)

        animate += Animation(opacity=1, duration=2)
        animate += Animation(opacity=0.7, size_hint= (1,1))
        animate += Animation(size_hint= (.5,.5))
        animate += Animation(pos_hint= {"center_x": 0.15})
        animate += Animation(pos_hint= {"center_x": 0.85})
        animate += Animation(pos_hint= {"center_x": 0.5})

        animate.start(widget)

        animate.bind(on_complete= self.my_callback)

    def my_callback(self, *args):
        self.ids.label_id.text = "Animation Complete!"


class AnimatedApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AnimatedApp().run()