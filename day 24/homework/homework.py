def add_numbers(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Invalid input"


def divide_larger_by_smaller(x, y):
    try:
        num1 = float(x)
        num2 = float(y)

        larger = max(num1, num2)
        smaller = min(num1, num2)

        if smaller == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return larger / smaller
    except ValueError:
        return "Invalid input"
    

   