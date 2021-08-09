# Alert Dialog Boxes
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

class Mainclass(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("adb.kv")

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                    title = "Pretty Neat, RIght ?!",
                    text = "This is Some Text.",
                    buttons = [
                        MDFlatButton(
                            text="CANCEL", on_release = self.close_dialog
                        ),
                        MDRectangleFlatButton(
                            text = "Yes, It's Neat", on_release = self.neat_dialog
                        ),
                    ],
                
                    )
        self.dialog.open()


    def close_dialog(self, obj):
        self.dialog.dismiss()

    def neat_dialog(self, obj):
        self.dialog.dismiss()
        self.root.ids.my_label.text = "Hello, There..."

Mainclass().run()

