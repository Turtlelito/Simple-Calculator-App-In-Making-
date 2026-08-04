# Logic py

# Imports
import math

# Previous Result
result = 0
just_calculated = False

# Numbers
def display_appender(display, value):
    display.insert("end", str(value))


def display_deleter(display):
    current_display = display.get()
    display.delete(len(current_display) - 1, "end")

def display_clear(display):
    display.delete(0, "end")


# Operations