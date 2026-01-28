from tkinter import filedialog
import time

def export_results(open_ports, closed_ports):
    file_path = filedialog.asksaveasfilename(
        title = "Porty scan results",
        defaultextension = ".txt",
        filetypes = [("Text files", "*.txt")]
    )

    if not file_path:
        return
    
    with open(file_path, "w", encoding = "utf-8") as f:
        f.write("PORT SCAN RESULTS\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated: {time.ctime()}\n\n")

        f.write("[ OPEN PORTS ]\n")
        for port, rtt, decoded_banner, response in open_ports:
            f.write(f"{port}/tcp OPEN | RTT {rtt}ms\n")
            if decoded_banner:
                f.write(f"{port}/tcp OPEN | RTT {rtt}ms | Banner: {decoded_banner}\n")
            elif response:
                f.write(f"{port}/tcp OPEN | RTT {rtt}ms | Response: {response}\n")

        f.write("\n")
        
        f.write("[ CLOSED PORTS ]\n")
        for port, rtt in closed_ports:
            f.write(f"{port}/tcp CLOSED | RTT {rtt}ms\n")
