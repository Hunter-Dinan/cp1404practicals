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

    def handle_convert_m_to_km(self, input_number):
        """docstring..."""
        miles_input = get_valid_number(input_number)
        self.output_label = str(miles_input * MILES_TO_KM_CONVERSION)

    def handle_increment(self, increment_value: int):
        """docstring..."""
        miles_input = get_valid_number(self.root.ids.input_number.text)
        miles_input += increment_value

        self.root.ids.input_number.text = str(miles_input)
        self.handle_convert_m_to_km(miles_input)


def get_valid_number(number_input):
    """docstring..."""
    try:
        number = int(number_input)
    except ValueError:
        number = 0
    return number


ConvertMilesToKmApp().run()
