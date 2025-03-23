def simple_calculator(num1, num2, operator):
    # Check if both num1 and num2 are numbers (either int or float)
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        return "unknown value"
    
    # Perform operation based on the operator
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Check for division by zero
        if num2 == 0:
            return "unknown value"
        return num1 / num2
    else:
        return "unknown value"
    

   