class Car:
    def __init__(self, registration_number, max_speed,):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.distance = 0
    
    def accelerate(self, speed):
        if self.cur_speed + speed > 0:
            if self.cur_speed + speed < self.max_speed:
                self.cur_speed += speed
            else:
                difference = self.max_speed - self.cur_speed 
                self.cur_speed += difference
        else:
            self.cur_speed = 0

car1 =Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f"speed after acceleration: {car1.cur_speed} km/h")

car1.accelerate(-200)

print(f"Speed after emergency brakes: {car1.cur_speed} km/h")


    