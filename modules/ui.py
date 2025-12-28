from customtkinter import *
import socket

def start_ui():
    app = CTk()
    app.geometry("600x500")
    app.title("Porty")
    app.resizable(False, False)

    address_input = CTkEntry(app, placeholder_text = "Target IP address", font = ("TkTextFont", 15), text_color = "white", width = 200)
    address_input.place(x = 10, y = 10)

    scan_button = CTkButton(app, text = "Scan", fg_color = "#6398ba", width = 100)
    scan_button.place(x = 220, y = 10)

    closed_label = CTkLabel(app, text = "Closed ports", font = ("TkTextFont", 20), text_color = "white")
    closed_label.place(x = 10, y = 60)

    closed_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 285, height = 250)
    closed_textbox.place(x = 10, y = 100)

    open_label = CTkLabel(app, text = "Open ports", font = ("TkTextFont", 20), text_color = "white")
    open_label.place(x = 300, y = 60)

    open_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 285, height = 250)
    open_textbox.place(x = 305, y = 100)

    app.mainloop()