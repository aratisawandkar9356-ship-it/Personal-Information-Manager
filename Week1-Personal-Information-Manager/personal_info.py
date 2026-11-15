
print("Welcome to Personal Information Manager!")

# Personal information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")

# Additional information
food = input("Enter your favourite food: ")
color = input("Enter your favourite color: ")

# Display information
print("\n----- Personal Information -----")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Age in months: {age * 12} months")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"Favourite Food: {food}")
print(f"Favourite Color: {color}")

print("\nThank you for using Personal Information Manager!")
