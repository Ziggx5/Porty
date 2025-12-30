import socket
import threading

def start_scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox):
    thread = threading.Thread(target = scan, args = (address, logs_textbox, closed_textbox, open_textbox, misc_textbox,))
    thread.start()

def scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox):
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)

        try:
            result = s.connect_ex((address, port))
            if result == 0:
                logs_textbox.insert("end", f"[>] Port {port} ... OPEN\n")
                open_textbox.insert("end", f"[>] Port {port} ... OPEN\n")
                open_textbox.see("end")
            elif result == 111:
                logs_textbox.insert("end", f"[>] Port {port} ... CLOSED\n")
                closed_textbox.insert("end", f"[>] Port {port} ... CLOSED\n")
                closed_textbox.see("end")
            elif result in (110, 11):
                logs_textbox.insert("end", f"[>] Port {port} ... FILTERED/NO RESPONSE\n")
                misc_textbox.insert("end", f"[>] Port {port} ... FILTERED/NO RESPONSE\n")
                misc_textbox.see("end")
            else:
                logs_textbox.insert("end", f"[>] Port {port} ... ERROR\n")
                misc_textbox.insert("end", f"[>] Port {port} ... FILTERED/NO RESPONSE\n")
                misc_textbox.see("end")
            logs_textbox.see("end")
        except:
            s.close()



