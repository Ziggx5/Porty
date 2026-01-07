import socket
import threading
from modules.scan_rate import rate

def start_scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar, stop_event, rate_input):
    stop_event.clear()
    thread = threading.Thread(target = scan, args = (address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar, stop_event, rate_input))
    thread.start()

def scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar, stop_event, rate_input):
    first = int(first_entry)
    second = int(second_entry)

    if first < 1 or second > 65535 or first > second:
        logs_textbox.insert("end", "[!] Invalid port range\n")
        return
    
    open_textbox.delete(0.0, "end")
    closed_textbox.delete(0.0, "end")
    misc_textbox.delete(0.0, "end")
    logs_textbox.delete(0.0, "end")

    total_ports = second - first + 1
    scanned_ports = 0

    for port in range(first, second + 1):
        if stop_event.is_set():
            logs_textbox.insert("end", "[!] Scan stopped by user\n")
            break
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(rate(rate_input))

        try:
            result = s.connect_ex((address, port))
            if result == 0:
                status = "OPEN"
                open_textbox.insert("end", f"[>] Port {port} ... OPEN\n")

            elif result in (111, 10061):
                status = "CLOSED"
                closed_textbox.insert("end", f"[>] Port {port} ... CLOSED\n")

            elif result in (110, 10060):
                status = "FILTERED / TIMEOUT"
                misc_textbox.insert("end", f"[>] Port {port} ... FILTERED / TIMEOUT\n")
            
            elif result in (11, 10035):
                status = "NO RESPONSE"
                misc_textbox.insert("end", f"[>] Port {port} ... NO RESPONSE\n")
            else:
                status = "ERROR"
                misc_textbox.insert("end", f"[>] Port {port} ... ERROR\n")
            
            logs_textbox.insert("end", f"[>] Port {port} ... {status}\n" )
            logs_textbox.see("end")
            open_textbox.see("end")
            closed_textbox.see("end")
            misc_textbox.see("end")

            scanned_ports += 1
            progress = scanned_ports / total_ports
            progress_bar.set(progress)
        finally:
            s.close()



