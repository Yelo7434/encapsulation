from pet import Pet

# Create a Pet object
pet_1 = Pet()

# Set values
pet_1.set_name("Yelo")
pet_1.set_animal_type("Cat")
pet_1.set_age(1)

# Display pet information
print("Pet Information")
print(f"Name: {pet_1.get_name()}")
print(f"Animal Type: {pet_1.get_animal_type()}")
print(f"Age: {pet_1.get_age()}")