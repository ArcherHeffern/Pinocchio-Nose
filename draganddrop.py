import tkinter as tk
from tkinter import ttk

class DragAndDrop(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack(fill=tk.BOTH, expand=1)

        label = ttk.Label(self, text='Drag and drop', background='white')
        label.pack(fill=tk.X, padx=5, pady=5)

        button = ttk.Button(self, text='Button')
        button.pack(padx=5, pady=5)

        # bind the left mouse button to the button for dragging
        button.bind('<ButtonPress-1>', self.on_button_press)
        button.bind('<B1-Motion>', self.on_button_motion)
        button.bind('<ButtonRelease-1>', self.on_button_release)

    def on_button_press(self, event):
        widget = event.widget
        widget.start_x = event.x
        widget.start_y = event.y
    def on_button_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.start_x + event.x
        y = widget.winfo_y() - widget.start_y + event.y
        widget.place(x=x, y=y)

    def on_button_release(self, event):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x150+300+300')
    root.title('Drag and Drop')
    DragAndDrop(root)
    root.mainloop()