# Weather Monitoring System

## Features

- Collects and stores weather data including temperature, humidity, and pressure.
- Supports multiple display devices such as mobile apps, web interfaces, and desktop applications.
- Notifies display devices automatically when the weather conditions change.
- Display devices update their own user interface and display the received weather data.
- New display devices can be added without modifying the existing code.
- Display devices can unsubscribe from the weather station if they no longer wish to receive updates.

## Components

The Weather Monitoring System consists of the following main components:

1. `WeatherStation`: Represents the subject and manages the registration, removal, and notification of display devices.
2. `DisplayDevice`: Acts as an observer and defines the interface for receiving weather updates.
3. `MobileAppDisplay`, `WebInterfaceDisplay`, `DesktopAppDisplay`: Concrete observers that implement the `DisplayDevice` interface and display weather information on different platforms.
4. `WeatherData`: Stores the weather information, including temperature, humidity, and pressure.




# Vehicle Factory

The Vehicle Factory is a Python application that demonstrates the Factory Method design pattern for creating different types of vehicles. It provides a way to encapsulate the creation logic of vehicles into separate factory classes, allowing the client code to create objects without knowing the specific class implementation.

## Features

- Creates different types of vehicles such as cars, motorcycles, and trucks.
- Uses separate factory classes to encapsulate the creation logic.
- Allows the client code to create vehicles without knowing their specific classes.
- Provides a common interface (`create_vehicle`) for creating vehicles.

## Components

The Vehicle Factory consists of the following main components:

1. `Vehicle`: Represents a generic vehicle with attributes like wheels, seating capacity, and maximum speed.
2. `VehicleFactory`: Serves as the Creator interface that declares the factory method (`create_vehicle`) for creating vehicles.
3. `Car`, `Motorcycle`, `Truck`: Concrete Product classes that inherit from `Vehicle` and provide specific implementations for creating different types of vehicles.
4. `CarFactory`, `MotorcycleFactory`, `TruckFactory`: Concrete Creator classes that implement the factory method (`create_vehicle`) to create specific types of vehicles.
