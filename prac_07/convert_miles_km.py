"""Kivy GUI program for converting miles to kilometres."""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM_CONVERSION = 1.609


class ConvertMilesToKmApp(App):
    """Kivy App for converting miles to kilometres."""
    output_label = StringProperty()

    def build(self):
        """Build Kivy App."""
        Window.size = (500, 200)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_mile_to_km(self, input_number):
        """Handle converting miles to kilometres."""
        miles_input = self.get_valid_number(input_number)
        self.output_label = str(miles_input * MILES_TO_KM_CONVERSION)

    def handle_increment(self, increment_value):
        """Handle incremental change in input text (from button or otherwise), and update input text."""
        miles_input = self.get_valid_number(self.root.ids.input_number.text)
        miles_input += increment_value

        self.root.ids.input_number.text = str(miles_input)
        # self.handle_convert_mile_to_km(miles_input)
        # Above is redundant with the button disabled and on_text in use

    @staticmethod
    def get_valid_number(number_input):
        """Convert input number to float or return 0.0."""
        try:
            number = float(number_input)
        except ValueError:
            number = 0.0
        return number


ConvertMilesToKmApp().run()
