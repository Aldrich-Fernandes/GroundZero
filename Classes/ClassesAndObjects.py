class Pin:
    TotalPins = 0 #static variable (same for all instances(objects) of the class) - similar to a global variable

    def __init__(self,pinName, pinLocation, pinMarker): # a constructor(method) for the attributes
        self.__name = pinName # '__' create a private attribute/method - It is non-static(specific to each instance) 
        self.__location = pinLocation
        self.__markerType = pinMarker
        Pin.addTotalPins()

    def returnData(self): # a constructor for returning the data (should do for private attributes)
        return self.__name, self.__location, self.__markerType 

    @classmethod # Static variable which is a constant that is same for all instances
    def addTotalPins(cls): # method that only works on the class and not on instances
        cls.TotalPins += 1

pins = []
for x in range(3):
    name = input("\nEnter pin name: ")
    location = str(input("Enter coordinates: ")).split(",")
    marker = input("Enter marker type: ")
    
    PinObject = Pin(name, location, marker) # Instances of the 'Pin' class
    pins.append(PinObject)

for pin in pins:
    print(pin.returnData())

print(Pin.TotalPins)

class Math:

    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def subtract(a,b):
        return a-b

    @staticmethod
    def pr():
        print("run")

print(Math.add(2,7))
print(Math.subtract(7,10))
Math.pr()