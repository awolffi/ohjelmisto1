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
    
    def drive(self, duration):
        self.distance = self.cur_speed = 

car1 =Car("ABC-123", 142)