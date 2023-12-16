
# calories_calculator.py

from constants import MALE_BMR_CONSTANT, FEMALE_BMR_CONSTANT, \
    SEDENTARY_MULTIPLIER, LIGHTLY_ACTIVE_MULTIPLIER

def calculate_bmr(age, gender, weight, height):
    if gender.lower() == 'male':
        bmr = MALE_BMR_CONSTANT + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        bmr = FEMALE_BMR_CONSTANT + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")
    
    return bmr

def calculate_tdee(bmr, activity_level):
    if activity_level.lower() == 'sedentary':
        tdee = bmr * SEDENTARY_MULTIPLIER
    elif activity_level.lower() == 'lightly active':
        tdee = bmr * LIGHTLY_ACTIVE_MULTIPLIER
    else:
        raise ValueError("Invalid activity level. Please enter 'sedentary' or 'lightly active'.")
    return tdee

def main():
    print("Welcome to the Calories Calculator!")
    print("Please provide the following information:")
    
    age = int(input("Age (in years): "))
    gender = input("Gender (male/female): ")
    weight = float(input("Weight (in kilograms): "))
    height = float(input("Height (in centimeters): "))
    activity_level = input("Activity Level (sedentary/lightly active): ")

    # Calculate BMR and TDEE
    bmr = calculate_bmr(age, gender, weight, height)
    tdee = calculate_tdee(bmr, activity_level)

    # Display results
    print("\nResults:")
    print(f"Basal Metabolic Rate (BMR): {bmr:.2f} calories/day")
    print(f"Total Daily Energy Expenditure (TDEE): {tdee:.2f} calories/day")

if __name__ == "__main__":
    main()
