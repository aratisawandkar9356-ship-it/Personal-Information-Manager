
# Personal Information Manager
# Week 1 Python Basics Project
# Created by: Arati Sawandkar

# Welcome message
print("=" * 40)
print("   PERSONAL INFORMATION MANAGER")
print("=" * 40)

# Personal information
name = "Arati Sawandkar"
age = 20
city = "Basmath"
hobby = "Music"

# Get information from user
print("\nPlease tell me about yourself!")

favorite_food = input("Enter your favorite food: ").strip()

while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("Enter your favorite food: ").strip()

favorite_color = input("Enter your favorite color: ").strip()

while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("Enter your favorite color: ").strip()

# Calculate age in months
age_in_months = age * 12

# Display information
print("\n" + "=" * 40)
print("       YOUR INFORMATION")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Favorite Food: {favorite_food.title()}")
print(f"Favorite Color: {favorite_color.title()}")

# Goodbye message
print("\n" + "=" * 40)
print("Thank you for using this program!")
print("=" * 40)
