'''Seven segment display of hex digits.'''
import tkinter as tk
root = tk.Tk()
screen = tk.Canvas(root)
screen.grid()

offsets = (
    (0, 0, 1, 0),  # top
    (1, 0, 1, 1),  # upper right
    (1, 1, 1, 2),  # lower right
    (0, 2, 1, 2),  # bottom
    (0, 1, 0, 2),  # lower left
    (0, 0, 0, 1),  # upper left
    (0, 1, 1, 1),  # middle
)

digits = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
    (1, 1, 1, 0, 1, 1, 1),  # A
    (0, 0, 1, 1, 1, 1, 1),  # B
    (1, 0, 0, 1, 1, 1, 0),  # C
    (0, 1, 1, 1, 1, 0, 1),  # D
    (1, 0, 0, 1, 1, 1, 1),  # E
    (1, 0, 0, 0, 1, 1, 1),  # F
    (1, 1, 1, 1, 0, 1, 1),  # G 
    (0, 0, 1, 0, 1, 1, 1),  # H
    (0, 0, 1, 0, 0, 0, 0),  # I
    (0, 1, 1, 1, 0, 0, 0),  # J
    (0, 0, 1, 0, 1, 1, 1),  # K
    (0, 0, 0, 0, 1, 1, 0),  # L
    (1, 0, 1, 0, 1, 0, 1),  # M
    (0, 0, 1, 0, 1, 0, 1),  # N
    (0, 0, 1, 1, 1, 0, 1),  # O
    (1, 1, 0, 0, 1, 1, 1),  # P
    (1, 1, 1, 0, 0, 1, 1),  # Q
    (0, 0, 0, 0, 1, 0, 1),  # R
    (1, 0, 1, 1, 0, 1, 1),  # S
    (0, 0, 0, 1, 1, 1, 1),  # T
    (0, 0, 1, 1, 1, 0, 0),  # U
    (0, 1, 0, 0, 0, 1, 1),  # V
    (0, 1, 0, 1, 0, 1, 1),  # X
    (0, 1, 0, 0, 1, 0, 1),  # Z
    (0, 1, 1, 0, 0, 1, 1),  # Y
    (1, 1, 0, 1, 1, 0, 1)   # W
)


class Digit:
    def __init__(self, canvas, *, x=10, y=10, length=20, width=3):
        self.canvas = canvas
        l = length
        self.segs = []
        for x0, y0, x1, y1 in offsets:
            self.segs.append(canvas.create_line(
                x + x0*l, y + y0*l, x + x1*l, y + y1*l,
                width=width, state = 'hidden'))
    def show(self, num):
        for iid, on in zip(self.segs, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')



dig = Digit(screen)
n = 0
def update():
    global n
    dig.show(n)
    n = (n+1) % 36
    root.after(1000, update)
root.after(1000, update)
root.mainloop()