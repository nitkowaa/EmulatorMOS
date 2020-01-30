import tkinter as tk
import gui
window = gui.Window("Hello")
btn = window.add_button("Click Me")
gui.on("btnPress", btn, lambda: print("Button Pressed."))
#If you don't know what lambda is, it just returns an anonymous, single expression function.
window.start()
