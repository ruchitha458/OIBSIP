def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator!")

try:
    weight = float(input("Enter your weight in kilograms: "))
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    
    height = float(input("Enter your height in meters: "))
    # 1 ft=0.3048m
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
