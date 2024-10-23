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

    

cars = []

for x in range(10):
    cars.append(Car("ABC-"+str(x+1), r.randint(100,200)))

race_hours = 0

while True:
    race_hours += 1
    for i in cars:
        acceleration = r.randint(-10, 16)
        i.cur_speed = acceleration
        i.drive(1)
        if i.distance > 10000:
            break

