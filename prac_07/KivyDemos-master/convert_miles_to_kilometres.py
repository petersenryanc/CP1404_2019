from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty


class MilestoKilometresApp(App):
    message = StringProperty()

    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_press(self):
        self.message = self.root.ids.user_input.text


MilestoKilometresApp().run()
