from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.result = TextInput(
            readonly=True,
            halign="right",
            font_size=55
        )
        self.add_widget(self.result)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["=", "x", "%", "00"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    font_size=32,
                    on_press=self.on_button_press
                )
                h_layout.add_widget(button)
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.result.text = ""
        elif text == "x":
            self.result.text = self.result.text[:-1]

        elif text == "=":
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = "Error"
        else:
            self.result.text += text


class CalculatorApp(App):
    def build(self):
        self.icon="calculator.png"
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()
