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


