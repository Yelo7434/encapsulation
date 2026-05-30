class Fan:
    # Levels of speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

# Construction
def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

# Getters
def get_speed(self):
        return self.__speed

def get_radius(self):
        return self.__radius

def get_color(self):
        return self.__color

def is_on(self):
        return self.__on

# Setters
def set_speed(self, speed):
        self.__speed = speed

def set_radius(self, radius):
        self.__radius = radius

def set_color(self, color):
        self.__color = color

def set_on(self, on):
        self.__on = on

# String representation
def __str__(self):
        if self.__on:
            return (
                f"Fan is ON\n"
                f"Speed: {self.__speed}\n"
                f"Radius: {self.__radius}\n"
                f"Color: {self.__color}\n"
            )

        return (
            f"Fan is OFF\n"
            f"Radius: {self.__radius}\n"
            f"Color: {self.__color}\n"
        )