from kivy.app import App
from kivy.lang import Builder

miles_km = 1.60934


class Conversion(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convet_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * miles_km
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):

        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):

        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


Conversion().run()
