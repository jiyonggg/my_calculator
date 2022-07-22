'''Tkinter Application'''
import tkinter as tk
from app.handler import *

class App:
    def __init__(self):
        '''Class Initializer'''
        self.rt_window = tk.Tk()
        self.rt_window.title("My Calculator")

        self.create_widgets()
        self.command_widgets()
        self.place_widgets()

        self.rt_window.mainloop()

    def create_widgets(self):
        '''Create Widgets'''
        BTN_WH = {"width":3, "height":1}

        # Frame
        self.frame = tk.Frame(self.rt_window)

        # Label
        self.label = tk.Label(self.frame, justify=tk.RIGHT)
        
        # Row 1
        self.entry = tk.Entry(self.frame, justify=tk.RIGHT, bg="black", fg="white")

        # Row 2
        self.btn_percent = tk.Button(self.frame, text='％', **BTN_WH)
        self.btn_clearexp = tk.Button(self.frame, text='CE', **BTN_WH)
        self.btn_clear = tk.Button(self.frame, text='C', **BTN_WH)
        self.btn_back = tk.Button(self.frame, text='←', **BTN_WH)
        
        # Row 3
        self.btn_fraction = tk.Button(self.frame, text='1/χ', **BTN_WH)
        self.btn_square = tk.Button(self.frame, text='χ²', **BTN_WH)
        self.btn_squareroot = tk.Button(self.frame, text='√χ', **BTN_WH)
        self.btn_divide = tk.Button(self.frame, text='÷', **BTN_WH)

        # Row 4
        self.btn_num7 = tk.Button(self.frame, text='7', **BTN_WH)
        self.btn_num8 = tk.Button(self.frame, text='8', **BTN_WH)
        self.btn_num9 = tk.Button(self.frame, text='9', **BTN_WH)
        self.btn_time = tk.Button(self.frame, text='×', **BTN_WH)

        # Row 5
        self.btn_num4 = tk.Button(self.frame, text='4', **BTN_WH)
        self.btn_num5 = tk.Button(self.frame, text='5', **BTN_WH)
        self.btn_num6 = tk.Button(self.frame, text='6', **BTN_WH)
        self.btn_minus = tk.Button(self.frame, text='－', **BTN_WH)

        # Row 6
        self.btn_num1 = tk.Button(self.frame, text='1', **BTN_WH)
        self.btn_num2 = tk.Button(self.frame, text='2', **BTN_WH)
        self.btn_num3 = tk.Button(self.frame, text='3', **BTN_WH)
        self.btn_plus = tk.Button(self.frame, text='＋', **BTN_WH)

        # Row 7
        self.btn_negate = tk.Button(self.frame, text='＋/－', **BTN_WH)
        self.btn_num0 = tk.Button(self.frame, text='0', **BTN_WH)
        self.btn_point = tk.Button(self.frame, text='.', **BTN_WH)
        self.btn_calc = tk.Button(self.frame, text='＝', **BTN_WH)

    def command_widgets(self):
        '''Configure The Command of Widgets'''
        num_button_list = [getattr(self, f"btn_num{i}") for i in range(0, 10)]
        operator_button_list = [getattr(self, f"btn_{i}") for i in ('plus', 'minus', 'time', 'divide')]

        # Solution: 'Capture Lambda'
        for num_button in num_button_list:
            num_button.configure(command=lambda num_button=num_button: callback_number(num_button['text'], self.entry))

        for operator_button in operator_button_list:
            operator_button.configure(command=lambda operator_button=operator_button: callback_operator(operator_button['text'], self.entry))

        self.btn_back.configure(command=lambda: callback_back(self.entry))
        self.btn_clear.configure(command=lambda: callback_clear(self.entry))
        self.btn_clearexp.configure(command=lambda: callback_clearexp(self.entry))
        self.btn_point.configure(command=lambda: callback_point(self.entry))
        self.btn_calc.configure(command=lambda: callback_calc(self.entry))

    def place_widgets(self):
        '''Place Widgets'''
        # Row 0
        self.label.grid(row=0, column=0, columnspan=4)
        
        # Row 1
        self.entry.grid(row=1, column=0, columnspan=4)

        # Row 2
        self.btn_percent.grid(row=2, column=0)
        self.btn_clearexp.grid(row=2, column=1)
        self.btn_clear.grid(row=2, column=2)
        self.btn_back.grid(row=2, column=3)
        
        # Row 3
        self.btn_fraction.grid(row=3, column=0)
        self.btn_square.grid(row=3, column=1)
        self.btn_squareroot.grid(row=3, column=2)
        self.btn_divide.grid(row=3, column=3)

        # Row 4
        self.btn_num7.grid(row=4, column=0)
        self.btn_num8.grid(row=4, column=1)
        self.btn_num9.grid(row=4, column=2)
        self.btn_time.grid(row=4, column=3)

        # Row 5
        self.btn_num4.grid(row=5, column=0)
        self.btn_num5.grid(row=5, column=1)
        self.btn_num6.grid(row=5, column=2)
        self.btn_minus.grid(row=5, column=3)

        # Row 6
        self.btn_num1.grid(row=6, column=0)
        self.btn_num2.grid(row=6, column=1)
        self.btn_num3.grid(row=6, column=2)
        self.btn_plus.grid(row=6, column=3)

        # Row 7
        self.btn_negate.grid(row=7, column=0)
        self.btn_num0.grid(row=7, column=1)
        self.btn_point.grid(row=7, column=2)
        self.btn_calc.grid(row=7, column=3)

        # Frame
        self.frame.pack()

def main():
    '''Run'''
    App()
