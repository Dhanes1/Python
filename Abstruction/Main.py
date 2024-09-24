from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def hover(self):
        pass
class PushButton(Button):
    def click(self):
        print("Push Button Click")
class RadioButton(Button):
    def click(self):
        print("Radio Button Click")
tombol=PushButton()
tombol1=RadioButton()

# tombol.click()
# tombol1.click()
tombol.hover()
tombol1.hover()