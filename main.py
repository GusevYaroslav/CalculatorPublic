"""
Calculator
"""

"""
library import
"""
import tkinter as tk
from functools import partial
import calculations

root = tk.Tk()

"""
constant declaration 
"""

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
ROOT_WIDTH = 510
ROOT_HEIGHT= 525

BTN_NAMES = (('1', '2', '3', '+'), ('4', '5', '6', '-'), ('7', '8', '9', '*'), ('.', '0', '/', '//'),
             ('(', ')', '^', '%'), ('=', '', '', ''))


"""
class declaration 
"""

class Button:

    """
    the Button class is responsible for creating buttons
    """

    def __init__(self,
                 root,
                 text,
                 font,
                 height,
                 width,
                 relief,
                 bd,
                 command,
                 row,
                 column,
                 padx,
                 pady):


        self.btn = tk.Button(root,
                             text=text,
                             font=font,
                             height=height,
                             width=width,
                             relief=relief,
                             bd=bd,
                             command=command)
        """     
            self.btn - creates buttons
            text  - sets the label text
            font - sets the font of the label
            height - sets the height of the button
            width - sets the width of the button
            relief - sets the button relief
            bd - sets the border size
            command - sets command
        """


        self.btn.grid(row=row,
                      column=column,
                      padx=padx,
                      pady=pady)
        """
            self.btn.grid - used for positioning
            row - line number, counting from zero
            column - column number, counting starts from zero
            padx and pady - horizontal and vertical padding, respectively, 
                            from the grid cell borders to the element borders
        """

class App:

    """
    the App class is responsible for forming the program interface
    """

    def __init__(self, root):
        self.root = root
        self.ent = tk.Entry(self.root, width=50)
        self.root.title('Калькулятор')
        self.calc = Calculator(self.ent)

    """
        parameters are set in __init__
    """

    def set_win(self):

        root_offset_x = (SCREEN_WIDTH - ROOT_WIDTH) // 2
        root_offset_y = (SCREEN_HEIGHT - ROOT_HEIGHT) // 2
        self.root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}+{root_offset_x}+{root_offset_y}')

    """
    def set_win - creates a window
        root_offset_x/y - sets the offset along the x and y axes, respectively
        self.root.geometry - the first two numbers in the geometry argument string specify the width and height 
                            of the window. The second pair of numbers indicates the 
                            offset on the screen along the x and y axes.
        self.root.geometry - creating window geometry                   
    """

    def create_but(self):
        for row_number in range(len(BTN_NAMES)):
            for col_number in range(len(BTN_NAMES[row_number])):
                name = BTN_NAMES[row_number][col_number]
                btn = Button(self.root,
                             text=name,
                             font = ('Arial', 13),
                             height = 3,
                             width= 7,
                             relief = tk.RAISED,
                             bd=5,
                             command=partial(self.calc.add_symbol, name),
                             row=row_number + 1,
                             column=col_number,
                             padx=1, pady=1)

    """
    def create_but - a function that sets parameters for creating buttons. 
                    Buttons are created by calling objects of the class Button
    """

    def run(self):
        self.set_win()
        self.ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.create_but()
        self.root.mainloop()

    """
    def run - main function, responsible for collecting window elements 
             and for rendering all its elements
    """


class Calculator:

    """
    the Calculator class is responsible for performing calculations and processing calculator commands
    """

    def __init__(self, ent):
        self.ent = ent

    """
        Calculator class initialization
    """

    def add_symbol(self, symbol):
        value = self.ent.get()

        if symbol != '=':
            value += symbol
        else:
            value = calculations.ret_val(value)
            value = int(value)
            #value = value // 10

        self.ent.delete(0, tk.END)
        self.ent.insert(0, value)

    """
    def add_symbol - responsible for making calculations and rounding the result
    """

if __name__ == '__main__':
    calculator = App(root)
    calculator.run()

    """
    program launch
    """
