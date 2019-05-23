from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.61


class MilestoKilometresApp(App):
    message = StringProperty()

    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_press(self):
        value = self.check_input()
        self.message = self.root.ids.user_input.text
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def check_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilestoKilometresApp().run()
