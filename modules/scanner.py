import socket
import threading

def start_scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar):
    thread = threading.Thread(target = scan, args = (address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar,))
    thread.start()

def scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar):
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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(s)
        s.settimeout(0.1)

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



