# GUI py

# Imports
import customtkinter as CTk

# GUI functions

# Display
def build_display(window):
    display = CTk.CTkEntry(window, 
                           width=380, 
                           height=100, 
                           font= ("Arial", 24), 
                           justify="right")
    display.grid(row=0, column=0, padx=10, pady=10, columnspan=9)
    build_number_buttons(window)



# Number buttons
def build_number_buttons(window):
    button_9 = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="9",
                             fg_color="#404040",
                             hover_color="#505050")
    button_9.grid(row=3, column=2, padx=5, pady=(10))

    button_8 = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="8",
                                fg_color="#404040",
                                hover_color="#505050")
    button_8.grid(row=3, column=1, padx=5, pady=(10))

    button_7 = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="7",
                             fg_color="#404040",
                             hover_color="#505050")
    button_7.grid(row=3, column=0, padx=5, pady=(10))

    button_6 = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="6",
                                fg_color="#404040",
                                hover_color="#505050")
    button_6.grid(row=4, column=2, padx=5, pady=10)

    button_5 = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="5",
                             fg_color="#404040",
                             hover_color="#505050")
    button_5.grid(row=4, column=1, padx=5, pady=10)

    button_4 = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="4",
                                fg_color="#404040",
                                hover_color="#505050")
    button_4.grid(row=4, column=0, padx=5, pady=10)

    button_3 = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="3",
                             fg_color="#404040",
                             hover_color="#505050")
    button_3.grid(row=5, column=2, padx=5, pady=10)

    button_2 = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="2",
                                fg_color="#404040",
                                hover_color="#505050")
    button_2.grid(row=5, column=1, padx=5, pady=10)

    button_1 = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="1",
                             fg_color="#404040",
                             hover_color="#505050")
    button_1.grid(row=5, column=0, padx=5, pady=10)

    button_0 = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="0",
                                fg_color="#404040",
                                hover_color="#505050")
    button_0.grid(row=6, column=0, padx=5, pady=10)
    build_operation_buttons(window)
    





# Operation buttons
def build_operation_buttons(window):
    button_clear = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="AC",
                             fg_color="#D32F2F",
                             hover_color="#F44336")
    button_clear.grid(row=2, column=0, padx=5, pady=(10, 10))

    button_percentage = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="%",
                             fg_color="#555555",
                             hover_color="#6B6B6B")
    button_percentage.grid(row=2, column=1, padx=5, pady=(10, 10))

    button_division = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="÷",
                                fg_color="#555555",
                                hover_color="#6B6B6B")
    button_division.grid(row=2, column=2, padx=5, pady=(10, 10))

    button_multiplication = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="x",
                             fg_color="#555555",
                             hover_color="#6B6B6B")
    button_multiplication.grid(row=2, column=3, padx=5, pady=(10, 10))

    button_subtraction = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="-",
                                fg_color="#555555",
                                hover_color="#6B6B6B")
    button_subtraction.grid(row=3, column=3, padx=5, pady=10)

    button_addition = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text="+",
                             fg_color="#555555",
                             hover_color="#6B6B6B")
    button_addition.grid(row=4, column=3, padx=5, pady=10)

    button_equals = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="=",
                                fg_color="#D32F2F",
                                hover_color="#F44336")
    button_equals.grid(row=6, column=3, padx=5, pady=10)

    button_period = CTk.CTkButton(window, 
                             width=70, 
                             height=70, 
                             font=("Arial", 30),
                             text=".",
                             fg_color="#555555",
                             hover_color="#6B6B6B")
    button_period.grid(row=5, column=3, padx=5, pady=10)

    button_delete = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="DEL",
                                fg_color="#555555",
                                hover_color="#6B6B6B")
    button_delete.grid(row=6, column=1, padx=5, pady=10)

    button_square_root = CTk.CTkButton(window, 
                                width=70, 
                                height=70, 
                                font=("Arial", 30),
                                text="√",
                                fg_color="#555555",
                                hover_color="#6B6B6B")
    button_square_root.grid(row=6, column=2, padx=5, pady=10)
    build_history_button(window)


# History button
def build_history_button(window):
    history_button = CTk.CTkButton(window, 
                            width=40, 
                            height=20, 
                            font=("Arial", 15),
                            text="History",
                            fg_color="#2E2E2E",
                            hover_color="#3E3E3E")
    history_button.grid(row=1, column=0, padx=2, pady=10)

