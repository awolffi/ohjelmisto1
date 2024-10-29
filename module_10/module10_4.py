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

class Race:
    def __init__(self, race_name, race_distance, car_list):
        self.race_name = race_name
        self.race_distance = race_distance
        self.car_list = car_list

    def hour_passes(self):
        for c in self.car_list:
            acceleration = r.randint(-10, 16)
            c.accelerate(acceleration)
            c.drive(1)

    def print_results(self, hour):
        print(f"\nHours passed: {hour}")
        self.car_list.sort(key=lambda c: c.distance, reverse=True)
        for i in self.car_list:
            print(f"Car: {i.registration_number} Current speed: {i.cur_speed} Top speed: {i.max_speed}km/h Distance driven: {i.distance}km")


    def race_finished(self):
        for c in self.car_list:
            if c.distance >= self.race_distance:
                return True
            else:
                return False
            
                
    
        

    
race_hours = 0
cars = []

for x in range(10):
    cars.append(Car("ABC-"+str(x+1), r.randint(100,200)))

super_race = Race("grand_demolition_derby", 8000, cars) 

race_finished = False
while race_finished == False:
    race_hours += 1
    super_race.hour_passes()
    race_finished = super_race.race_finished()
    if race_hours % 10 == 0:
        super_race.print_results(race_hours)

print(f"\nthe race is over... the results are:", end="")
super_race.print_results(race_hours)





