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
        finally:
            s.close()



