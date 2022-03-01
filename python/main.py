import serial
import time


class SerialContainer:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
        self.ser = serial.Serial(port=port, baudrate=baudrate)

    def write(self, message):
        self.ser.write(message.encode("utf-8"))


class LedContainer:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):
        self.serial_container = SerialContainer(port=port, baudrate=baudrate)
        self.led_values = [0, 0, 0, 0, 0, 0]

    def set_value(self, led_pin, led_value):
        self.led_values[led_pin] = led_value
        message = f".{led_pin + 1} {led_value + 1}"
        self.serial_container.write(message)

    def set_values(self):
        for led_pin, led_value in enumerate(self.led_values):
            self.set_value(led_pin, led_value)

class LedAnimation:

    def __init__(self):
        self.led_container = LedContainer()
        self.led_container.set_values()
        self.animation_state = 0
        self.animation_direction = "up"

    def step(self):
        if self.animation_direction == "up":
            if self.animation_state < 255:
                self.animation_state += 1
                for i in range(6):
                    self.led_container.set_value(i, self.animation_state)
            else:
                self.animation_direction = "down"
        if self.animation_direction == "down":
            if self.animation_state > 0:
                self.animation_state -= 1
                for i in range(6):
                    self.led_container.set_value(i, self.animation_state)
            else:
                self.animation_direction = "up"




if __name__ == "__main__":
    led_animation = LedAnimation()
    while True:
        led_animation.step()
        time.sleep(0.01)