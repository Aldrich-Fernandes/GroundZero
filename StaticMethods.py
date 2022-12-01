
class Math:

    @staticmethod # dont have access to instances and dont change
    def add(a,b):
        return a + b
    
    @staticmethod
    def subtract(a,b):
        return a-b

    @staticmethod
    def pr():
        print("run")

print(Math.add(2,7)) # the Math class dosen't need any instance
print(Math.subtract(7,10))
Math.pr()