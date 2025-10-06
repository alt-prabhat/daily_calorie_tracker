# Name: Prabhat Bhatia
# Date: 04/10/2025
# Project: Daily Calorie Tracker CLI

from datetime import datetime 

# Task 1: Welcome Message
print("\n--- Daily Calorie Tracker CLI by Prabhat Bhatia ---")
print("\n=> Enter your meals and their calorie values.")

# Task 2: Input & Store data
meal_names = []
calorie_val = []

daily_lim = float(input("\nEnter your daily calorie limit: "))

num_meals = int(input("How many meals do you want to enter:"))
for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Meal name: ")
    calories = float(input(f"Calories for {meal}: "))
    meal_names.append(meal)
    calorie_val.append(calories)

# Task 3: Calorie calculations
total_cal = sum(calorie_val)
if calorie_val:
    avg_cal = total_cal / len(calorie_val)

# Task 4: Limit exceeding Warning system
if total_cal > daily_lim:
    wrn = "WARNING: Daily calorie limit exceeded!"
else:
    wrn = "SAFE: Within daily calorie limit."

# Task 5: Formatted outputs using \t and \n
print("\nMeal Name \t\t\t Calories:")
print("-"*50)
for i in range(len(meal_names)):
    print(f"{meal_names[i]} \t\t\t {calorie_val[i]} cal")
print(f"\nTotal calories: {total_cal}")
print(f"Average calories: {avg_cal}")
print(wrn)

# Task 6: Saving logs to a text file using file handling
sve = input("\nDo you want to save this report? (Y/N): ").lower()
if sve == 'y':
    with open("calorie_log.txt", "w") as f:
        f.write(f"CALORIE TRACKER LOG - {datetime.now()}\n")
        f.write(f"Daily Calorie Limit: {daily_lim}\n\n")
        f.write("Meal Name \t\t\t Calories \n")
        for i in range(len(meal_names)):
            f.write(f"{meal_names[i]}: \t\t\t {calorie_val[i]} cal \n\n")
        f.write(f"Total calories: {total_cal}\n")
        f.write(f"Average calories: {avg_cal}\n")
        f.write(f"{wrn}\n")
    print("\nSaved to calorie_log.txt.")
else:
    print("\nReport not saved.")