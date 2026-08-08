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
                        current_display.rfind("÷"))

    current_number = current_display[last_operator + 1:]

    if "." not in current_number:
        display.insert("end", ".")

def display_operations_appender(display, operator):
    current_display = display.get()

    if current_display == "":
            return
    
    last_character = current_display[-1]

    

    if last_character not in ["%", "÷", "x", "+", "-", "."]:
        display.insert("end", operator)

