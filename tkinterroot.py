from logging import root
from textwrap import fill
from tkinter import*

root=Tk()

root.title('canvas')
Canvas=Canvas(root,width=400,height=400)
Canvas.create_polygon(205,105,285,125,166,177,210,199,205,105,fill='red')
Canvas.pack()
root.mainloop()