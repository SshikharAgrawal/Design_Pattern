# Weather Station (Subject)
class WeatherStation:
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_weather_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


# Display Device (Observer)
class DisplayDevice:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError


# Mobile App Display (Concrete Observer)
class MobileAppDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"Mobile App Display: Temperature - {temperature}, Humidity - {humidity}, Pressure - {pressure}")


# Web Interface Display (Concrete Observer)
class WebInterfaceDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"Web Interface Display: Temperature - {temperature}, Humidity - {humidity}, Pressure - {pressure}")


# Desktop Application Display (Concrete Observer)
class DesktopAppDisplay(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print(f"Desktop Application Display: Temperature - {temperature}, Humidity - {humidity}, Pressure - {pressure}")


# Usage
if __name__ == "__main__":
    # Create the Weather Station
    weather_station = WeatherStation()

    # Create display devices (observers)
    mobile_app_display = MobileAppDisplay()
    web_interface_display = WebInterfaceDisplay()
    desktop_app_display = DesktopAppDisplay()

    # Subscribe display devices to the weather station
    weather_station.add_observer(mobile_app_display)
    weather_station.add_observer(web_interface_display)
    weather_station.add_observer(desktop_app_display)

    # Set weather data and notify observers
    weather_station.set_weather_data(25.5, 70, 1013.2)
