print("\n--- TASK 2: NUMBERS ---")

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
