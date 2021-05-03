"""Kivy GUI that greets the user when they input their name."""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App for greeting user."""
    def build(self):
        """Build Kivy app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting text."""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle clearing the output."""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
