"""
get_filename.py

This script will open a file dialog window and return the path of the selected
file as a string
"""

import tkinter as tk
from tkinter import filedialog

def give_filename():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()

    return path
