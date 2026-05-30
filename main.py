from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton

class KewaTestApp(MDApp):
    def build(self):
        # Green theme setup karte hain
        self.theme_cls.primary_palette = "Green"
        
        screen = MDScreen()
        
        # Ek simple button jo screen ke beech mein hoga
        btn = MDRaisedButton(
            text="Kewa App Tayyar Hai!",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        screen.add_widget(btn)
        return screen

if __name__ == "__main__":
    KewaTestApp().run()
