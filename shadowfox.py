# Beginner Python Tasks – ShadowFox Internship
# Contains 5 tasks: Variables, Numbers, Lists, If Conditions, For Loop

print("\n==================== TASK 1: VARIABLES ====================")

pi = 22/7
print("Value of pi:", pi, "| Type:", type(pi))

print("Cannot assign a value to 'for' because it is a reserved keyword.")

P = 15000  # Principal
R = 7      # Rate of Interest
T = 3      # Time (years)
simple_interest = (P * R * T) / 100
print("Simple Interest =", simple_interest)


print("\n==================== TASK 2: NUMBERS ====================")

num = 145
formatted = format(num, 'o')
print("Octal representation of 145:", formatted)

radius = 84
pi = 3.14
area = pi * (radius ** 2)
water_per_sqm = 1.4
water_total = int(area * water_per_sqm)
print("Area of pond:", round(area, 2))
print("Total water in liters:", water_total)

distance = 490
time_seconds = 7 * 60
speed = int(distance / time_seconds)
print("Speed in m/s:", speed)


print("\n==================== TASK 3: LISTS ====================")

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original team:", justice_league)

print("Number of members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl & Nightwing:", justice_league)

if "Wonder Woman" in justice_league:
    justice_league.remove("Wonder Woman")
    justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

if "Aquaman" in justice_league and "Flash" in justice_league:
    flash_index = justice_league.index("Flash")
    if "Superman" in justice_league:
        justice_league.insert(flash_index, "Superman")
print("After separating Aquaman & Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

justice_league.sort()
print("Sorted team:", justice_league)

