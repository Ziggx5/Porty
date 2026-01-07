from customtkinter import *
from modules.scanner import scan, start_scan
import threading

def start_ui():
    app = CTk()
    app.geometry("895x700")
    app.title("Porty")
    app.resizable(False, False)
    stop_event = threading.Event()

    address_input = CTkEntry(app, placeholder_text = "Target IP address", font = ("TkTextFont", 15), text_color = "white", width = 200)
    address_input.place(x = 10, y = 10)

    closed_textbox = CTkTextbox(app, font = ("TkTextFont", 15), width = 285, height = 250, text_color = "#E06C75", padx = 5, pady = 5)
    closed_textbox.place(x = 10, y = 100)

    open_textbox = CTkTextbox(app, font = ("TkTextFont", 15), width = 285, height = 250, text_color = "#98C379", padx = 5, pady = 5)
    open_textbox.place(x = 305, y = 100)

    misc_textbox = CTkTextbox(app, font = ("TkTextFont", 15), width = 285, height = 250, text_color = "#E5C07B", padx = 5, pady = 5)
    misc_textbox.place(x = 600, y = 100)

    logs_textbox = CTkTextbox(app, font = ("TkTextFont", 15), text_color = "white", width = 875, height = 250, padx = 5, pady = 5)
    logs_textbox.place(x = 10, y = 380)

    range_label = CTkLabel(app, text = "Port range:", font = ("TkTextFont", 15), text_color = "white")
    range_label.place(x = 630, y = 10)

    first_entry = CTkEntry(app, placeholder_text = "1", font = ("TkTextFont", 15), text_color = "white", width = 70)
    first_entry.place(x = 720, y = 10)

    minus_label = CTkLabel(app, text = "-", font = ("TkTextFont", 15), text_color = "white")
    minus_label.place(x = 800, y = 10)

    second_entry = CTkEntry(app, placeholder_text = "65535", font = ("TkTextFont", 15), text_color = "white", width = 70)
    second_entry.place(x = 815, y = 10)

    progress_bar = CTkProgressBar(app, width = 310, progress_color = "green")
    progress_bar.place(x = 10, y = 60)
    progress_bar.set(0)
    percentage_label = CTkLabel(app, text = "0%", font = ("TkTextFont", 15), text_color = "white")
    percentage_label.place(x = 330, y = 50)

    stop_button = CTkButton(app, text = "Stop", fg_color = "#fc2d2d", width = 100, height = 30, hover_color = "#7d1515", command = lambda: stop_event.set())
    stop_button.place(x = 330, y = 10)

    scan_rate_label = CTkLabel(app, text = "Scan rate:", font = ("TkTextFont", 15), text_color = "white")
    scan_rate_label.place(x = 630, y = 50)

    rate_input = CTkEntry(app, placeholder_text = "0.1", font = ("TkTextFont", 15), text_color = "white", width = 70)
    rate_input.place(x = 720, y = 50)

    second_label = CTkLabel(app, text = "s", font = ("TkTextFont", 15), text_color = "white")
    second_label.place(x = 800, y = 50)

    scan_button = CTkButton(app, text = "Scan", fg_color = "#0673bd", hover_color = "#033e66", width = 100, height = 30, command = lambda: start_scan(address_input.get(), logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry.get(), second_entry.get(), progress_bar, stop_event, rate_input.get(), percentage_label))
    scan_button.place(x = 220, y = 10)

    app.mainloop()