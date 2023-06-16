# Vehicle (Product)
class Vehicle:
    def __init__(self, wheels, seating_capacity, maximum_speed):
        self.wheels = wheels
        self.seating_capacity = seating_capacity
        self.maximum_speed = maximum_speed

    def display_info(self):
        print(f"Wheels: {self.wheels}")
        print(f"Seating Capacity: {self.seating_capacity}")
        print(f"Maximum Speed: {self.maximum_speed}")


# Vehicle Factory (Creator)
class VehicleFactory:
    def create_vehicle(self):
        raise NotImplementedError


# Car (Concrete Product)
class Car(Vehicle):
    def __init__(self):
        super().__init__(4, 5, 200)


# Motorcycle (Concrete Product)
class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(2, 1, 180)


# Truck (Concrete Product)
class Truck(Vehicle):
    def __init__(self):
        super().__init__(6, 2, 120)


# Car Factory (Concrete Creator)
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


# Motorcycle Factory (Concrete Creator)
class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()


# Truck Factory (Concrete Creator)
class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()


# Usage
if __name__ == "__main__":
    # Prompt user for the type of vehicle they want to manufacture
    vehicle_type = input("Enter the type of vehicle (car, motorcycle, truck): ")

    # Create the appropriate factory based on the user's input
    if vehicle_type == "car":
        factory = CarFactory()
    elif vehicle_type == "motorcycle":
        factory = MotorcycleFactory()
    elif vehicle_type == "truck":
        factory = TruckFactory()
    else:
        print("Invalid vehicle type.")
        exit()

    # Use the factory to create the desired vehicle
    vehicle = factory.create_vehicle()

    # Display the attributes of the manufactured vehicle
    vehicle.display_info()
