import math

print("""
  ____      _            _       _              
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __  
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| 
| |__| (_| | | (__| |_| | | (_| | || (_) | |    
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    

         Advanced Calculator
---------------------------------------------
Operators: +, -, *, /, ^, %, //, sqrt, abs,
           log, log10, sin, cos, tan, !, last
Type 'exit' to quit
---------------------------------------------
""")

last_result = None

def factorial(n):
    if n < 0 or int(n) != n:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(int(n))

while True:
    try:
        val1_input = input("First number (or 'last'): ").strip()
        if val1_input.lower() == "exit":
            print("Goodbye!")
            break
        value1 = last_result if val1_input.lower() == "last" else float(val1_input)

        operator = input("Operator: ").strip().lower()

        if operator in ["sqrt", "abs", "log", "log10", "sin", "cos", "tan", "!"]:
            # Single-argument operations
            if operator == "sqrt":
                if value1 < 0:
                    print("Error: Cannot take square root of negative number.")
                    continue
                result = math.sqrt(value1)
            elif operator == "abs":
                result = abs(value1)
            elif operator == "log":
                if value1 <= 0:
                    print("Error: Logarithm only defined for positive numbers.")
                    continue
                result = math.log(value1)
            elif operator == "log10":
                if value1 <= 0:
                    print("Error: Logarithm only defined for positive numbers.")
                    continue
                result = math.log10(value1)
            elif operator == "sin":
                result = math.sin(math.radians(value1))
            elif operator == "cos":
                result = math.cos(math.radians(value1))
            elif operator == "tan":
                result = math.tan(math.radians(value1))
            elif operator == "!":
                result = factorial(value1)
        else:
            val2_input = input("Second number (or 'last'): ").strip()
            if val2_input.lower() == "exit":
                print("Goodbye!")
                break
            value2 = last_result if val2_input.lower() == "last" else float(val2_input)

            if operator == "+":
                result = value1 + value2
            elif operator == "-":
                result = value1 - value2
            elif operator == "*":
                result = value1 * value2
            elif operator == "/":
                if value2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = value1 / value2
            elif operator == "^":
                result = value1 ** value2
            elif operator == "%":
                result = value1 % value2
            elif operator == "//":
                if value2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = value1 // value2
            else:
                print("Error: Unknown operator.")
                continue

        result = round(result, 6)
        last_result = result
        print("Result:", result)

    except ValueError as e:
        print("Error:", e)
