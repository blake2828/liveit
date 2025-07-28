import tkinter as tk
from tkinter import ttk, messagebox
import math
import pyperclip
import re

def calculate(self):
    try:
        expr = self.result_var.get()

        # Replace math functions with math library equivalents
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("log10", "math.log10")
        expr = expr.replace("^", "**")

        # Wrap sin, cos, tan arguments with math.radians()
        expr = re.sub(r"sin\((.*?)\)", r"math.sin(math.radians(\1))", expr)
        expr = re.sub(r"cos\((.*?)\)", r"math.cos(math.radians(\1))", expr)
        expr = re.sub(r"tan\((.*?)\)", r"math.tan(math.radians(\1))", expr)

        result = eval(expr)
        self.result_var.set(str(result))
        self.add_to_history(self.result_var.get() + " = " + str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression:\n{e}")


class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Fun Calculator 😎")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.history = []
        self.is_dark = False

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.result_var = tk.StringVar()

        # Entry widget to display expression/result
        self.entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), justify="right")
        self.entry.pack(fill="x", padx=10, pady=10, ipady=10)

        # Buttons and layout
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["sin", "cos", "tan", "sqrt"],
            ["log", "^", "pi", "e"],
            ["C", "⌫", "Copy", "Theme"]
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(fill="x")
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=("Arial", 16), width=6, height=2, command=lambda b=btn_text: self.on_click(b))
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        # History panel
        self.history_box = tk.Text(self.root, height=8, state='disabled', bg='#f0f0f0')
        self.history_box.pack(fill="both", padx=10, pady=(5, 10))

    def bind_keys(self):
        self.root.bind("<Return>", lambda e: self.on_click("="))
        self.root.bind("<BackSpace>", lambda e: self.on_click("⌫"))
        self.root.bind("<Delete>", lambda e: self.on_click("C"))
        for key in "0123456789.+-*/":
            self.root.bind(key, lambda e, k=key: self.on_click(k))

    def on_click(self, char):
        if char == "C":
            self.result_var.set("")
        elif char == "⌫":
            self.result_var.set(self.result_var.get()[:-1])
        elif char == "Copy":
            pyperclip.copy(self.result_var.get())
        elif char == "Theme":
            self.toggle_theme()
        elif char == "=":
            self.calculate()
        elif char == "pi":
            self.result_var.set(self.result_var.get() + str(math.pi))
        elif char == "e":
            self.result_var.set(self.result_var.get() + str(math.e))
        elif char == "sqrt":
            self.result_var.set(self.result_var.get() + "sqrt(")
        elif char == "log":
            self.result_var.set(self.result_var.get() + "log10(")
        elif char == "^":
            self.result_var.set(self.result_var.get() + "**")
        elif char in ["sin", "cos", "tan"]:
            self.result_var.set(self.result_var.get() + f"{char}(")
        else:
            self.result_var.set(self.result_var.get() + char)

    def calculate(self):
        try:
            expr = self.result_var.get()
            expr = expr.replace("sqrt", "math.sqrt")
            expr = expr.replace("log10", "math.log10")
            expr = expr.replace("sin", "math.sin")
            expr = expr.replace("cos", "math.cos")
            expr = expr.replace("tan", "math.tan")
            result = eval(expr)
            self.result_var.set(str(result))
            self.add_to_history(expr + " = " + str(result))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression: {e}")

    def add_to_history(self, entry):
        self.history.append(entry)
        self.history_box.configure(state='normal')
        self.history_box.insert('end', entry + "\n")
        self.history_box.configure(state='disabled')
        self.history_box.see('end')

    def toggle_theme(self):
        if not self.is_dark:
            self.root.configure(bg="black")
            self.history_box.configure(bg="gray20", fg="white")
            self.entry.configure(background="black", foreground="white")
        else:
            self.root.configure(bg="SystemButtonFace")
            self.history_box.configure(bg="#f0f0f0", fg="black")
            self.entry.configure(background="white", foreground="black")
        self.is_dark = not self.is_dark

if __name__ == "__main__":
    import pyperclip  # Ensure pyperclip is available (pip install pyperclip)
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()
