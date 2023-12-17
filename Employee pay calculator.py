import tkinter as tk
from tkinter import messagebox

def calculate_pay():
    try:
        # Get input values from the entry fields
        name = name_entry.get()
        hourly_wage = float(hourly_wage_entry.get())
        regular_hours = float(regular_hours_entry.get())
        overtime_hours = float(overtime_hours_entry.get())

        # Calculate gross pay
        regular_pay = hourly_wage * regular_hours
        overtime_pay = hourly_wage * 1.5 * overtime_hours
        gross_pay = regular_pay + overtime_pay

        # Calculate superannuation deduction
        superannuation = gross_pay * 0.05

        # Calculate net pay
        net_pay = gross_pay - superannuation

        # Update the output labels
        gross_pay_label.config(text=f"Total Gross Pay: ${gross_pay:.2f}")
        superannuation_label.config(text=f"Superannuation Contribution: ${superannuation:.2f}")
        net_pay_label.config(text=f"Total Weekly Net Pay: ${net_pay:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for hourly wage, regular hours, and overtime hours.")

# Create the main window
window = tk.Tk()
window.title("Employee Pay Calculator")

# Create and place labels and entry fields
name_label = tk.Label(window, text="Employee Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

hourly_wage_label = tk.Label(window, text="Hourly Wage:")
hourly_wage_label.pack()
hourly_wage_entry = tk.Entry(window)
hourly_wage_entry.pack()

regular_hours_label = tk.Label(window, text="Total Regular Hours:")
regular_hours_label.pack()
regular_hours_entry = tk.Entry(window)
regular_hours_entry.pack()

overtime_hours_label = tk.Label(window, text="Total Overtime Hours:")
overtime_hours_label.pack()
overtime_hours_entry = tk.Entry(window)
overtime_hours_entry.pack()

calculate_button = tk.Button(window, text="Calculate Pay", command=calculate_pay)
calculate_button.pack()

# Create and place output labels
gross_pay_label = tk.Label(window)
gross_pay_label.pack()

superannuation_label = tk.Label(window)
superannuation_label.pack()

net_pay_label = tk.Label(window)
net_pay_label.pack()

# Start the main event loop
window.mainloop()