from customtkinter import *
from modules.scanner import scan, start_scan

def start_ui():
    app = CTk()
    app.geometry("895x700")
    app.title("Porty")
    app.resizable(False, False)

    address_input = CTkEntry(app, placeholder_text = "Target IP address", font = ("TkTextFont", 15), text_color = "white", width = 200)
    address_input.place(x = 10, y = 10)

    closed_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 285, height = 250)
    closed_textbox.place(x = 10, y = 100)

    open_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 285, height = 250)
    open_textbox.place(x = 305, y = 100)

    misc_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 285, height = 250)
    misc_textbox.place(x = 600, y = 100)

    logs_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 875, height = 250)
    logs_textbox.place(x = 10, y = 380)

    scan_button = CTkButton(app, text = "Scan", fg_color = "#6398ba", width = 100, command = lambda: start_scan(address_input.get(), logs_textbox, closed_textbox, open_textbox, misc_textbox))
    scan_button.place(x = 220, y = 10)

    app.mainloop()