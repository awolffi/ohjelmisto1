class Elevator:
    def __init__(self, bottom_floor, top_floor, num):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        self.num = num
    #checks if the floor selection is valid
    
    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor or floor == self.current_floor:
            print("invalid input")
            return
        #moves to the selected floor one at a time
        while self.current_floor != floor:
            if self.current_floor < floor:
                Elevator.floor_up(self, 1)
                print(f"current floor is {self.current_floor}")
            elif self.current_floor > floor:
                Elevator.floor_down(self, 1)
                print(f"current floor is {self.current_floor}")
        
        else:
            print(f"You have arrived to floor {self.current_floor} with elevator number {self.num}")

    def floor_up(self, floor):
        self.current_floor += floor
    
    def floor_down(self, floor):
        self.current_floor -= floor


class Building:
    def __init__(self, lowest_floor, highest_floor, elevator_count):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevator_count = elevator_count
        self.elevators = []
    
        for i in range(self.elevator_count):
            self.elevators.append(Elevator(self.lowest_floor, self.highest_floor, i))
        
    def run_elevator(self, num, destination):
        self.elevators[num].go_to_floor(destination)

    def fire_alarm(self):
        print("fire alarm activated. sending all elevators down")
        for f in self.elevators:
            f.go_to_floor(1)
            

tower = Building(1, 25, 5)

tower.run_elevator(4, 15)
tower.run_elevator(3, 8)
tower.run_elevator(2, 3)
tower.run_elevator(1, 7)
tower.run_elevator(0, 22)

tower.fire_alarm()