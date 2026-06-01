from car import Car
# Create a Car object
car_1 = Car(2025, "Tesla Model S")

print("Car Information")
print(f"Year Model: {car_1.get_year_model()}")
print(f"Make: {car_1.get_make()}")

print("\nAccelerating...")
for count in range(5):
    car_1.accelerate()
    print(f"Current Speed: {car_1.get_speed()} mph")

print("\nBraking...")
for count in range(5):
    car_1.brake()
    print(f"Current Speed: {car_1.get_speed()} mph")