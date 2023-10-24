from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.label import Label
from random import randint, choice


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        # Создаю экран и кнопку
        screen = MDScreen()
        button = MDRectangleFlatButton(
            text="Hello, World",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        screen.add_widget(button)

        # Генерирую случайные символы и добавляю их в случайные места на экране
        random_chars = [chr(randint(33, 126)) for _ in range(10)]
        for char in random_chars:
            for _ in range(2):
                random_x = randint(0, 100)
                random_y = randint(0, 100)
                label = Label(
                    text=char,
                    pos_hint={"x": random_x / 100, "y": random_y / 100}
                )
                screen.add_widget(label)

        return screen


MainApp().run()
