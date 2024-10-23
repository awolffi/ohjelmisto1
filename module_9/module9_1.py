class Car:
    def __init__(self, registration_number, max_speed,):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.distance = 0

car1 = Car("ABC-123", 142)

print(f"Registration number: {car1.registration_number}, max speed: {car1.max_speed}, current speed: {car1.cur_speed}km/h, distance: {car1.distance}")
    