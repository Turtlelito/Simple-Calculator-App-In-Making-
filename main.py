# Main Py

# Imports
import customtkinter as CTk
import gui

# Window Configuration
CTk.set_appearance_mode("Dark")
CTk.set_default_color_theme("blue")

# Window Creation
calculator_window = CTk.CTk()
calculator_window.title("Calculator App")
calculator_window.geometry("400x600")
calculator_window.resizable(False, False)


# GUI Creation
gui.build_display(calculator_window)

# Starts and maintains program
calculator_window.mainloop()


