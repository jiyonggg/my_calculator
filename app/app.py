'''Tkinter Application'''
import tkinter as tk
from app.handler import *

class App:
    def __init__(self):
        self.rt_window = tk.Tk()
        self.rt_window.title("My Calculator")

        self.create_widgets()
        self.place_widgets()

        self.rt_window.mainloop()

    def create_widgets(self):
        '''Create Widgets'''
        BTN_WH = {"width":3, "height":1}

        # Frame
        self.frame = tk.Frame(self.rt_window)
        
        # Row 0
        self.entry = tk.Entry(self.frame, justify=tk.RIGHT)

        # Row 1
        self.btn_percent = tk.Button(self.frame, text='％', **BTN_WH)
        self.btn_temp = tk.Button(self.frame, text=' ', **BTN_WH)
        self.btn_clear = tk.Button(self.frame, text='C', **BTN_WH)
        self.btn_back = tk.Button(self.frame, command=lambda: callback_back(self.entry), text='←', **BTN_WH)
        
        # Row 2
        self.btn_temp2 = tk.Button(self.frame, text=' ', **BTN_WH)
        self.btn_temp3 = tk.Button(self.frame, text=' ', **BTN_WH)
        self.btn_temp4 = tk.Button(self.frame, text=' ', **BTN_WH)
        self.btn_divide = tk.Button(self.frame, text='÷', **BTN_WH)

        # Row 3
        self.btn_num7 = tk.Button(self.frame, command=lambda: callback_number('7', self.entry), text='7', **BTN_WH)
        self.btn_num8 = tk.Button(self.frame, command=lambda: callback_number('8', self.entry), text='8', **BTN_WH)
        self.btn_num9 = tk.Button(self.frame, command=lambda: callback_number('9', self.entry), text='9', **BTN_WH)
        self.btn_time = tk.Button(self.frame, text='×', **BTN_WH)

        # Row 4
        self.btn_num4 = tk.Button(self.frame, command=lambda: callback_number('4', self.entry), text='4', **BTN_WH)
        self.btn_num5 = tk.Button(self.frame, command=lambda: callback_number('5', self.entry), text='5', **BTN_WH)
        self.btn_num6 = tk.Button(self.frame, command=lambda: callback_number('6', self.entry), text='6', **BTN_WH)
        self.btn_minus = tk.Button(self.frame, text='－', **BTN_WH)
        self.btn_minus

        # Row 5
        self.btn_num1 = tk.Button(self.frame, command=lambda: callback_number('1', self.entry), text='1', **BTN_WH)
        self.btn_num2 = tk.Button(self.frame, command=lambda: callback_number('2', self.entry), text='2', **BTN_WH)
        self.btn_num3 = tk.Button(self.frame, command=lambda: callback_number('3', self.entry), text='3', **BTN_WH)
        self.btn_plus = tk.Button(self.frame, text='＋', **BTN_WH)

        # Row 6
        self.btn_temp5 = tk.Button(self.frame, text=' ', **BTN_WH)
        self.btn_num0 = tk.Button(self.frame, command=lambda: callback_number('0', self.entry), text='0', **BTN_WH)
        self.btn_point = tk.Button(self.frame, text='.', **BTN_WH)
        self.btn_calc = tk.Button(self.frame, text='＝', **BTN_WH)

    def place_widgets(self):
        '''Place Widgets'''
        # Row 0
        self.entry.grid(row=0, column=0, columnspan=4)

        # Row 1
        self.btn_percent.grid(row=1, column=0)
        self.btn_temp.grid(row=1, column=1)
        self.btn_clear.grid(row=1, column=2)
        self.btn_back.grid(row=1, column=3)
        
        # Row 2
        self.btn_temp2.grid(row=2, column=0)
        self.btn_temp3.grid(row=2, column=1)
        self.btn_temp4.grid(row=2, column=2)
        self.btn_divide.grid(row=2, column=3)

        # Row 3
        self.btn_num7.grid(row=3, column=0)
        self.btn_num8.grid(row=3, column=1)
        self.btn_num9.grid(row=3, column=2)
        self.btn_time.grid(row=3, column=3)

        # Row 4
        self.btn_num4.grid(row=4, column=0)
        self.btn_num5.grid(row=4, column=1)
        self.btn_num6.grid(row=4, column=2)
        self.btn_minus.grid(row=4, column=3)

        # Row 5
        self.btn_num1.grid(row=5, column=0)
        self.btn_num2.grid(row=5, column=1)
        self.btn_num3.grid(row=5, column=2)
        self.btn_plus.grid(row=5, column=3)

        # Row 6
        self.btn_temp5.grid(row=6, column=0)
        self.btn_num0.grid(row=6, column=1)
        self.btn_point.grid(row=6, column=2)
        self.btn_calc.grid(row=6, column=3)

        # Frame
        self.frame.pack()

def main():
    '''Run'''
    App()
