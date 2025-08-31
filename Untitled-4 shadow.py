print("\n===== TASK 4: IF CONDITIONS =====")

# 4.1 BMI Category
height = 1.75  # meters
weight = 70    # kilograms
BMI = weight / (height ** 2)

if BMI >= 30:
    category = "Obesity"
elif BMI >= 25:
    category = "Overweight"
elif BMI >= 18.5:
    category = "Normal"
else:
    category = "Underweight"

print(f"BMI: {BMI:.2f}, Category: {category}")

# 4.2 City to Country
city = "Dubai"
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the given list")
