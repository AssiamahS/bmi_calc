def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    return bmr * activity_multipliers[activity_level]

def calculate_macros(tdee):
    protein = 0.3 * tdee / 4  # 30% of calories from protein
    fat = 0.25 * tdee / 9     # 25% of calories from fat
    carbs = 0.45 * tdee / 4   # 45% of calories from carbs
    return protein, fat, carbs

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ").lower()

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    protein, fat, carbs = calculate_macros(tdee)

    print(f"Your BMR is: {bmr:.2f} calories/day")
    print(f"Your TDEE is: {tdee:.2f} calories/day")
    print(f"Macronutrient goals (in grams per day):")
    print(f"Protein: {protein:.2f}g")
    print(f"Fat: {fat:.2f}g")
    print(f"Carbohydrates: {carbs:.2f}g")

if __name__ == "__main__":
    main()
