from abc import ABC, abstractmethod
class electronic(ABC):
    @abstractmethod
    def off(self):
        pass
class tablet(electronic):
    def on(self):
        print("Tablet can turn on")
class phone(electronic):
    def on(self):
        print("Phone can turn on")
tablet().on()
phone().on()