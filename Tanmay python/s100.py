class Car (object):
    def __init__(self,model, company , color , numberplate):
        self.model=model
        self.company=company
        self.color=color
        self.numberplate=numberplate
    def start(self):
        print('car started')
    def stop(self):
        print('car stopped') 
    def axclerate (self):
        print('car axclerated')
Volvo=Car('xc90', 'Volvo', 'pearl white', '0001')
print(Volvo.color)
print(Car.start(Volvo)) 

print(Volvo.model)
print(Car.start (Volvo))

print(Volvo.numberplate)
print(Car.stop (Volvo))            