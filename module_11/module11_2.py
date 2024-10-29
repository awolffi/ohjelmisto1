import random as r
class Car:
    def __init__(self, registration_number, max_speed,):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.distance = 0

    def __str__(self):
        return f"{self.registration_number}, {self.max_speed}"
    
    def accelerate(self, speed):
        if self.cur_speed + speed > 0:
            if self.cur_speed + speed < self.max_speed:
                self.cur_speed += speed
            else:
                difference = self.max_speed - self.cur_speed 
                self.cur_speed += difference
        else:
            self.cur_speed = 0
    
    def drive(self, duration):
        self.distance += self.cur_speed * duration

class ElectricCar(Car):
    def __init__(self, battery, registration_number, max_speed):
        self.battery = battery
        super().__init__(registration_number, max_speed)
        
        
class GasolineCar(Car):
    def __init__(self, volume, registration_number, max_speed):
        self.volume = volume
        super().__init__(registration_number, max_speed)

cars = []
cars.append(GasolineCar(32.3, "ACD-123", 165))
cars.append(ElectricCar(52.5, "ABC-15", 52.5))

for f in cars:
    speed = r.randint(50, 150)
    f.accelerate(speed)
    f.drive(3)
    print(f"car with {f.registration_number} reg number dove for {f.distance} km")


