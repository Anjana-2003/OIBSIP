#TASK-2: BMI Calculator 
#Author: Anjana Chaturvedi
#Batch:  August-P1
#Domain: Python Programming
#Aim:-   Create a command-line BMI calculator in Python. Prompt users for their weight (in kilograms) and height (in meters).
#Calculate the BMI and classify it into categories (e.g., underweight, normal, overweight) based on predefined ranges.
#Display the BMI result and category to the user.
def calculate_bmi(weight, height):
    """Calculate BMI based on weight (kg) and height (m)"""
    bmi = weight / (height ** 2)
    print(bmi)
    return bmi

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
