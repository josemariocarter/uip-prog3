from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Calculadora(BoxLayout):
    def resultado(self, express):
        if not express: return

        try:

            self.pantalla.text = str(eval(express))

        except Exception:
            self.pantalla.text = 'Error'


class CalculadoraApp(App):
    title = 'Calculadora Proyecto'
    icon = 'icono.png'

    def build(self):
        return Calculadora()

if __name__ in '__main__':
    CalculadoraApp().run()
