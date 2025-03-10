class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spots = capacity
        self.parking_state = [0] * capacity

    def park_car(self):
        if self.available_spots > 0:
            for i in range(self.capacity):
                if self.parking_state[i] == 0:
                    self.parking_state[i] = 1
                    self.available_spots -= 1
                    print(f"Masina parcata la locul {i + 1}.")
                    return
        print("Parcarea este plina!")

    def leave_parking(self, spot):
        if 1 <= spot <= self.capacity and self.parking_state[spot - 1] == 1:
            self.parking_state[spot - 1] = 0
            self.available_spots += 1
            print(f"Masina plecata de la locul {spot}.")
        else:
            print("Loc invalid sau deja liber!")

    def display_status(self):
        print(f"Locuri disponibile: {self.available_spots}/{self.capacity}")
        print("Starea parcarii:", self.parking_state)
        
if __name__ == "__main__":
    parking_lot = ParkingLot(5)
    parking_lot.display_status()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.display_status()
    parking_lot.leave_parking(1)
    parking_lot.display_status()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.park_car()
    parking_lot.display_status()
    parking_lot.leave_parking(3)
    parking_lot.display_status()
