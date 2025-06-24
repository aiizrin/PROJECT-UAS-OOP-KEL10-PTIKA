from abc import ABC, abstractmethod

class ProsesProduksi(ABC):
    @abstractmethod
    def adon(self):
        pass

    @abstractmethod
    def kembangkan(self):
        pass

    @abstractmethod
    def panggang(self):
        pass

    @abstractmethod
    def topping(self):
        pass