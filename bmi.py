def calculate_bmi(weight, height):
    """
    Calculate the BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m))^2
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value according to the standard categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {interpretation}")