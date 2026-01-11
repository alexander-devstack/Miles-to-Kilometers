# Miles to Kilometers Converter (Tkinter)

This repository contains a simple miles‑to‑kilometers converter built with Python and Tkinter. It is my first GUI project, created to explore Tkinter widgets like `Entry`, `Label`, and `Button` and understand how to connect user input, a calculation function, and live output in a small desktop app.[file:337]

---

## App Overview

- A small window titled **"Mile to Km Converter"**.
- An input field where the user types a distance in miles.
- A **Calculate** button that converts miles to kilometers using the factor `1.60934`.
- A label that updates to show the converted value in kilometers.[file:337]

This project focuses on learning how Tkinter layouts, commands, and widget interactions work.

---

## File

- `miles-to-km.py`  
  - Imports Tkinter (`from tkinter import *`).  
  - Defines `miles_to_km()`:
    - Reads the value from the `Entry` widget with `input.get()`.
    - Converts it to `float` and multiplies by `1.60934`.
    - Updates the `output` label text with the result.[file:337]  
  - Creates the main `Tk()` window:
    - Sets the title and minimal size.
    - Adds padding using `window.config(padx=150, pady=90)`.  
  - Builds the UI:
    - `Entry` widget for miles input, placed with `grid`.
    - `Label` for the numeric result (initially `0`).
    - `Button` labeled **"Calculate"** that triggers `miles_to_km` when clicked.
    - Text labels for `"Miles"`, `"Km"`, and `"is equal to"` for clarity.[file:337]  
  - Calls `window.mainloop()` to start the Tkinter event loop and keep the window open.

---

## Requirements

- Python 3.10 or higher.
- Tkinter (included with standard Python on most systems).

No external libraries are required.

---

## How to Run

1. Save `miles-to-km.py` in a folder of your choice.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python miles-to-km.py
4.Type a value in miles in the input field and click on the calculate button to view the converted answer

##Possible Improvements
1.Add input validation and error messages for non‑numeric input.
2.Format the output to a fixed number of decimal places.
3.Improve the layout with additional spacing or fonts.
4.Expand the converter to support more unit types (e.g., km ↔ miles, meters, etc.).

This small project serves as a first step into building graphical desktop applications with Tkinter.





   
