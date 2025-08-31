print("\n===== TASK 5: FOR LOOP =====")

import random

# Roll the dice 20 times
dice_rolls = [random.randint(1, 6) for _ in range(20)]
print("Dice rolls:", dice_rolls)

# Count how many 6s and 1s
count_6 = dice_rolls.count(6)
count_1 = dice_rolls.count(1)

# Count consecutive 6s
two_6s_in_a_row = 0
for i in range(len(dice_rolls) - 1):
    if dice_rolls[i] == 6 and dice_rolls[i + 1] == 6:
        two_6s_in_a_row += 1

print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Two 6s in a row:", two_6s_in_a_row)
