from fan import Fan
# First fan object
fan_1 = Fan()
fan_1.set_speed(Fan.FAST)
fan_1.set_radius(10)
fan_1.set_color("yellow")
fan_1.set_on(True)

# Second fan object
fan_2 = Fan()
fan_2.set_speed(Fan.MEDIUM)
fan_2.set_radius(5)
fan_2.set_color("blue")
fan_2.set_on(False)

# Display fan information
print("FIRST FAN")
print(fan_1)

print("SECOND FAN")
print(fan_2)