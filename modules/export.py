from tkinter import filedialog
import time

def export_results(open_ports, closed_ports):
    file_path = filedialog.asksaveasfile(
        title = "Porty scan results",
        defaultextension = ".txt",
        filetypes = [{"*.txt"}]
    )

    if not file_path:
        return