
class Car:
    def __init__(self,maker,model):
        self.maker = maker
        self.model = model
        self.starting = False
    
    def start_engine(self):
        self.starting = True
        return(f"starting the {self.maker}{self.model} enigner")
        
    def stop_engine(self):
        self.starting = False
        return(f"stoping the {self.maker}{self.model} enigner")
        
car = Car("Honda","Amaze")
other_car = Car("Tata","Innova")

print(car.start_engine())
print(car.starting)
print(other_car.starting)