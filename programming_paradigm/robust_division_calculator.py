
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result =  num / den
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Cannot divide by zero."
    except ValueError:
        return "Invalid input. Please enter numeric values."