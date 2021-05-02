"""Kivy GUI program for generating labels dynamically from a list."""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelGeneratorApp(App):
    """Kivy app for generating labels dynamically from a list."""
    def __init__(self):
        """Initialise Dynamic Label Generator."""
        super().__init__()
        self.names = ['Hunter', 'James', 'Jerry', 'Sam', 'Ryan', 'Julien']

    def build(self):
        """Build Kivy App."""
        self.title = 'Dynamic Label Generator'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the names list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelGeneratorApp().run()
