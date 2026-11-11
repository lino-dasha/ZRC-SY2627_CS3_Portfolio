from abc import ABC, abstractmethod

class Sensor (ABC):

    @abstractmethod
    def get_reading (self):
        pass

class PHSensor (Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")

class TempSensor (Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5C")
        
phsensor = PHSensor()
tempsensor = TempSensor()
print("--- Lab Inventory System ---")
phsensor.get_reading()
tempsensor.get_reading()

my_Sensor = Sensor() 