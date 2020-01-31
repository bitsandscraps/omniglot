import os

import numpy as np
import tkinter
from PIL import Image, ImageTk


def view(dirname: str, tk: tkinter.Tk):
    old = None
    for root, _, files in os.walk(dirname):
        if not files:
            continue
        path = os.path.join(root, files[0])
        try:
            image = Image.open(path, 'r')
            tk.geometry('105x105')
            tkpi = ImageTk.PhotoImage(image)
            label_image = tkinter.Label(tk, image=tkpi)
            label_image.place(x=0, y=0, width=105, height=105)
            tk.title(path)
            if old is not None:
                old.destroy()
            old = label_image
            tk.mainloop()
        except IOError:
            pass



if __name__ == "__main__":
    tk = tkinter.Tk()
    tk.bind("<Button>", lambda e: e.widget.quit())
    tk.geometry('+100+100')
    view('images_background', tk)
    view('images_evaluation', tk)
