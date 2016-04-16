"""
Alexander Cerrud 8-850-2381
Luís Wong 8-894-456
Pedro perez se 1788657
Humberto Caceres 8-875-1617
Miguel Tejada 8-868-1026
Jose mario carter 8-915-1458
Bonilla jose luis 8-886-2453
Mario Martínez 062905639
David Acevedo 8924137
Boris montalvo 8-848-1016"""""
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
