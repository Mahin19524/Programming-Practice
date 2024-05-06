import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x500")

        # Entry widget to display input and output
        self.entry = ttk.Entry(root, width=40, font=('Arial', 14), justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Define buttons layout and text
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create and place buttons
        for (text, row, column) in buttons:
            button = ttk.Button(root, text=text, width=10, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

        # Clear and backspace buttons
        clear_button = ttk.Button(root, text='C', width=10, command=self.button_clear)
        clear_button.grid(row=5, column=0, padx=5, pady=5)

        backspace_button = ttk.Button(root, text='⌫', width=10, command=self.button_backspace)
        backspace_button.grid(row=5, column=1, padx=5, pady=5)

        # Equal button
        equal_button = ttk.Button(root, text='=', width=10, command=self.button_equal)
        equal_button.grid(row=5, column=2, padx=5, pady=5)

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.entry.delete(0, tk.END)

    def button_backspace(self):
        current = self.entry.get()[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current)

    def button_equal(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
