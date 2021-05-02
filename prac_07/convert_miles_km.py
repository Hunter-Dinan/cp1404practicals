"""Module Docstring..."""

from kivy.app import App
from kivy.app import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM_CONVERSION = 1.609


class ConvertMilesToKmApp(App):
    """docstring..."""
    output_label = StringProperty()

    def build(self):
        """docstring..."""
        Window.size = (500, 200)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_m_to_km(self, input_number: int):
        """docstring..."""
        self.output_label = str(input_number * MILES_TO_KM_CONVERSION)

    def handle_increment(self, increment_value: int):
        """docstring..."""
        miles_input = int(self.root.ids.input_number.text)
        miles_input += increment_value

        self.root.ids.input_number.text = str(miles_input)
        self.handle_convert_m_to_km(miles_input)


ConvertMilesToKmApp().run()
