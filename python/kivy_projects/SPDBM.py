from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):

    data= {
        "Python": "language-python",
        "Ruby": "language-ruby",
        "Java Script": "language-javascript"

    }
    
    def callback(self, instance):
        self.root.ids.my_label.text = f"You Pressed {instance.icon}"


    def open(self):
        self.root.ids.my_label.text = "Open!"

    
    def close(self):
        self.root.ids.my_label.text = "Closed"


    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("spdbm.kv")


MainApp().run()
            