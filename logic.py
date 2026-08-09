# Logic py

# Imports
import math

# Previous Result
result = 0
just_calculated = False

# Numbers
def display_numbers_appender(display, value):
    display.insert("end", str(value))


# Deleters
def display_deleter(display):
    current_display = display.get()
    display.delete(len(current_display) - 1, "end")

def display_clear(display):
    display.delete(0, "end")


# Operations
def display_decimal_appender(display):
    current_display = display.get()

    if current_display == "":
         return
    
    last_operator = max(current_display.rfind("+"),
                        current_display.rfind("-"),
                        current_display.rfind("x",),
                        current_display.rfind("÷"),
                        current_display.rfind("%"))

    current_number = current_display[last_operator + 1:]
    last_character = current_display[-1]

    if "." not in current_number:
        if last_character not in ["%", "÷", "x", "+", "-", ".", "%"]:
            display.insert("end", ".")
        

def display_operations_appender(display, operator):
    current_display = display.get()
    operators = ["%", "÷", "x", "+", "-", ".", "%"]

    if current_display == "":
        return

    if any(operator in current_display for operator in operators):
        return
    
    last_operation = current_display[-1]

    

    if last_operation not in ["%", "÷", "x", "+", "-", ".", "%"]:
        display.insert("end", operator)

def calculate_operation(display):
    current_display = display.get()
    operator_index = max(current_display.rfind("+"),
                        current_display.rfind("-"),
                        current_display.rfind("x",),
                        current_display.rfind("÷"),
                        current_display.rfind("%"))
    left_string = current_display[:operator_index]
    right_string = current_display[operator_index + 1:]
    left_number = float(left_string)
    right_number = float(right_string)
    operator = None
    answer = 0

    if "+" in current_display:
        operator = "+"
    elif "-" in current_display:
        operator = "-"
    elif "x" in current_display:
        operator = "x"
    elif "÷" in current_display:
        operator = "÷"
    elif "%" in current_display:
        operator = "%"

    if operator == "+":
        answer += left_number + right_number
    elif operator == "-":
        answer += left_number - right_number
    elif operator == "x":
        answer += left_number * right_number
    elif operator == "÷":
        answer += left_number / right_number
    elif operator == "%":
        answer += left_number % right_number

    display.delete(0, "end")
    display.insert("end", str(answer))


    if current_display == "":
        return


    return(answer)


