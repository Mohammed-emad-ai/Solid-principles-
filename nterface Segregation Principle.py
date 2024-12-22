from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

class VolumeControl(ABC):
    @abstractmethod
    def set_volume(self, volume):
        pass

class LightingControl(ABC):
    @abstractmethod
    def set_lighting(self, color):
        pass

class Guitar(Instrument, VolumeControl):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.volume = 5 

    def play(self):
        print(f"Playing the guitar: {self.make} {self.model}")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Guitar volume set to: {self.volume}")

class Piano(Instrument):
    def __init__(self, brand):
        self.brand = brand

    def play(self):
        print(f"Playing the piano: {self.brand}")

class DiscoGuitar(Instrument, VolumeControl, LightingControl):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.volume = 5 
        self.light_color = "white"

    def play(self):
        print(f"Playing the disco guitar: {self.make} {self.model}")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Disco Guitar volume set to: {self.volume}")

    def set_lighting(self, color):
        self.light_color = color
        print(f"Disco Guitar lighting color set to: {self.light_color}")


guitar = Guitar("pppp", "pppp")
guitar.play()
guitar.set_volume(7)

piano = Piano("Yamaha")
piano.play()

disco_guitar = DiscoGuitar("gh", "Les")
disco_guitar.play()
disco_guitar.set_volume(10)
disco_guitar.set_lighting("red")