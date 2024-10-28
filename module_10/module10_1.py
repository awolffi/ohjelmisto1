class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
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
            print(f"You have arrived to floor {self.current_floor}")
                


    def floor_up(self, floor):
        self.current_floor += floor
    
    def floor_down(self, floor):
        self.current_floor -= floor


hissi = Elevator(1, 15)
hissi.go_to_floor(5)
hissi.go_to_floor(11)
hissi.go_to_floor(11)

