import random as r
import time

class Car:
    def __init__(self, register, top_speed,):
        self.register = register
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance = 0
    
    # Accelerate changes the Cars current speed
    def accelerate(self,kmh):
        # Checks if combined speed is less than 0
        if self.current_speed + kmh > 0:
            # Checks if current speed and new speed is more than top speed
            if self.current_speed + kmh < self.top_speed:
                self.current_speed += kmh
            # Checks how much left till top speed is met and adds it 
            else:
                top_to_curr = self.top_speed - self.current_speed
                self.current_speed += top_to_curr
        # if new speed would be less than 0, make speed 0
        else:
            self.current_speed = 0
    
    # Travel calculates how many km has been traveled in given amount of hours
    def travel(self,hour):
        self.distance += self.current_speed * hour

class Race:
    def __init__(self, name, lenght_km, car_list):
        self.name = name
        self.lenght_km = lenght_km
        self.car_list = car_list
        

    def hour_passed(self):
        for car in self.car_list:
            acceleration = r.randint(-10, 15)
            car.accelerate(acceleration)
            car.travel(1)
        
        
        

    def print_result(self,hour):
        print(f"\nHours passed: {hour}")
        self.car_list.sort(key=lambda c: c.distance, reverse=True)
        for c in self.car_list:
            print(f"Car: {c.register:8} Current Speed {c.current_speed:3.0f}; Top Speed {c.top_speed:3.0f}km/h; Distance {c.distance:7}km")
        time.sleep(0.5)

    def race_over(self):
        for car in self.car_list:
            if car.distance >= self.lenght_km:
                return True
            else:
                return False

        
        
        
cars = []
total_hours = 0
# Loop for car generation
for c in range(10):
    cars.append(Car("ABC-"+str(c+1), r.randint(100,200)))


great_derby = Race("Great Derby", 8000, cars)

print("The race is starting, here are our cars!")
for c in cars:
    print(f"Car: {c.register:8} Top Speed {c.top_speed:3.0f}km/h")
time.sleep(2)

race_over = False
while race_over == False:
    total_hours += 1
    great_derby.hour_passed()
    race_over = great_derby.race_over()
    if total_hours % 10 == 0:
        great_derby.print_result(total_hours)

print("\nThe race is over!", end="")
great_derby.print_result(total_hours)


# self.car_list.sort(key=lambda c: c.distance, reverse=True)
#         for c in self.car_list:
#             print(f"Car: {c.register:8} Current Speed {c.current_speed:3.0f}; Top Speed {c.top_speed:3.0f}km/h; Distance {c.distance:7}km")