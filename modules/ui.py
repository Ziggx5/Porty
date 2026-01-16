from customtkinter import *
from modules.scanner import scan, start_scan
import threading
import os
from PIL import Image, ImageTk

def start_ui():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    images_path = os.path.join(root, "images")
    icon_path = os.path.join(images_path, "icon.png")
    icon = Image.open(icon_path)
    
    app = CTk()
    app.geometry("1490x750")
    app.title("Porty")
    app.resizable(False, False)
    app.iconphoto(False, ImageTk.PhotoImage(icon))
    stop_event = threading.Event()

    logs_frame = CTkFrame(app)
    logs_frame.place(x = 10, y = 450)

    closed_frame = CTkFrame(app)
    closed_frame.place(x = 10, y = 150)

    open_frame = CTkFrame(app)
    open_frame.place(x = 380, y = 150)

    misc_frame = CTkFrame(app)
    misc_frame.place(x = 750, y = 150)

    filtered_frame = CTkFrame(app)
    filtered_frame.place(x = 1120, y = 150)

    address_input = CTkEntry(
        app,
        placeholder_text = "Target IP",
        font = ("TkTextFont", 15),
        text_color = "white",
        width = 200
    )
    address_input.place(x = 10, y = 10)

    closed_label = CTkLabel(
        closed_frame,
        text = "Closed ports",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    closed_label.grid(row = 0, column = 0, sticky = "w", padx = 5)

    closed_textbox = CTkTextbox(
        closed_frame,
        font = ("TkTextFont", 15),
        width = 350,
        height = 250,
        text_color = "#E06C75",
        padx = 5,
        pady = 5
    )
    closed_textbox.grid(row = 1, column = 0, padx = 5, pady = 5)

    open_label = CTkLabel(
        open_frame,
        text = "Open ports",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    open_label.grid(row = 0, column = 0, sticky = "w", padx = 5)

    open_textbox = CTkTextbox(
        open_frame,
        font = ("TkTextFont", 15),
        width = 350,
        height = 250,
        text_color = "#98C379",
        padx = 5,
        pady = 5
    )
    open_textbox.grid(row = 1, column = 0, padx = 5, pady = 5)

    misc_label = CTkLabel(
        misc_frame,
        text = "No response",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    misc_label.grid(row = 0, column = 0, sticky = "w", padx = 5)

    misc_textbox = CTkTextbox(
        misc_frame,
        font = ("TkTextFont", 15),
        width = 350,
        height = 250,
        text_color = "#E5C07B",
        padx = 5,
        pady = 5
    )
    misc_textbox.grid(row = 1, column = 0, padx = 5, pady = 5)

    filtered_label = CTkLabel(
        filtered_frame,
        text = "Filtered / timeout",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    filtered_label.grid(row = 0, column = 0, sticky = "w", padx = 5)

    filtered_textbox = CTkTextbox(
        filtered_frame,
        font = ("TkTextFont", 15),
        width = 350,
        height = 250,
        text_color = "#E5C07B",
        padx = 5,
        pady = 5
    )
    filtered_textbox.grid(row = 1, column = 0, padx = 5, pady = 5)

    logs_label = CTkLabel(
        logs_frame,
        text = "Logs",
        font = ("TkTextFont", 15),
        text_color = "white"
    )

    logs_label.grid(row = 0, column = 0, sticky = "w", padx = 5)

    logs_textbox = CTkTextbox(
        logs_frame,
        font = ("TkTextFont", 15),
        text_color = "white",
        width = 1460,
        height = 250,
        padx = 5,
        pady = 5
    )
    logs_textbox.grid(row = 1, column = 0, padx = 5, pady = 5)

    range_label = CTkLabel(
        app,
        text = "Port range:",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    range_label.place(x = 1225, y = 10)

    first_entry = CTkEntry(
        app,
        placeholder_text = "1",
        font = ("TkTextFont", 15),
        text_color = "white",
        width = 70
    )
    first_entry.place(x = 1315, y = 10)

    minus_label = CTkLabel(
        app,
        text = "-",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    minus_label.place(x = 1395, y = 10)

    second_entry = CTkEntry(
        app,
        placeholder_text = "65535",
        font = ("TkTextFont", 15),
        text_color = "white",
        width = 70
    )
    second_entry.place(x = 1410, y = 10)

    progress_bar = CTkProgressBar(
        app,
        width = 310,
        progress_color = "green"
    )
    progress_bar.place(x = 10, y = 60)
    progress_bar.set(0)

    percentage_label = CTkLabel(
        app,
        text = "0%",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    percentage_label.place(x = 330, y = 50)

    stop_button = CTkButton(
        app,
        text = "Stop",
        fg_color = "#751414",
        width = 100,
        height = 30,
        state = "disabled",
        command = lambda: stop_event.set()
    )
    stop_button.place(x = 330, y = 10)

    scan_rate_label = CTkLabel(
        app,
        text = "Scan rate:",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    scan_rate_label.place(x = 1225, y = 50)

    rate_input = CTkEntry(
        app,
        placeholder_text = "0.1",
        font = ("TkTextFont", 15),
        text_color = "white",
        width = 70
    )
    rate_input.place(x = 1315, y = 50)

    second_label = CTkLabel(
        app,
        text = "s",
        font = ("TkTextFont", 15),
        text_color = "white"
    )
    second_label.place(x = 1395, y = 50)

    service_detection_check = CTkCheckBox(
        app,
        text = "Service detection",
        font = ("TkTextFont", 15),
        text_color = "white",
        fg_color = "#51c41f",
        hover_color = "#265c0f"
    )
    service_detection_check.place(x = 1225, y = 90)

    scan_button = CTkButton(
        app,
        text = "Scan",
        fg_color = "#0673bd",
        hover_color = "#033e66",
        width = 100,
        height = 30,
        command = lambda: start_scan(
            address_input.get(),
            logs_textbox,
            closed_textbox,
            open_textbox,
            misc_textbox,
            filtered_textbox,
            first_entry.get(),
            second_entry.get(),
            progress_bar,
            stop_event,
            rate_input.get(),
            percentage_label,
            stop_button,
            scan_button,
            service_detection_check.get()
            )
    )
    scan_button.place(x = 220, y = 10)

    app.mainloop()