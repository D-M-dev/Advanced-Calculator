# Python calculator with repeat
print("""
  ____      _            _       _             
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __  
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| 
| |__| (_| | | (__| |_| | | (_| | || (_) | |    
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    
""")

while True:
    try:
        value1 = float(input("First number: "))
        value2 = float(input("Second number: "))
        operator = input("Operator (+, -, *, /): ")

        if operator == "+":
            print("Result:", value1 + value2)
        elif operator == "-":
            print("Result:", value1 - value2)
        elif operator == "*":
            print("Result:", value1 * value2)
        elif operator == "/":
            if value2 == 0:
                print("Error: Division by zero is not possible.")
            else:
                print("Result:", value1 / value2)
        else:
            print("Error: Unknown operator.")

    except ValueError:
        print("Error: Invalid number entered.")

    #ask if you want to continue
    again = input("Do you want to continue ?").lower()
    if again != "yes":
        print("Thanks for using my calculator")
        break