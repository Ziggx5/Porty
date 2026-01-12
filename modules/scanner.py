import socket
import threading
from modules.scan_rate import rate
import time

def start_scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar, stop_event, rate_input, percentage_label):
    stop_event.clear()
    thread = threading.Thread(target = scan, args = (address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar, stop_event, rate_input, percentage_label,))
    thread.start()

def scan(address, logs_textbox, closed_textbox, open_textbox, misc_textbox, first_entry, second_entry, progress_bar, stop_event, rate_input, percentage_label):
    open_textbox.delete(0.0, "end")
    closed_textbox.delete(0.0, "end")
    misc_textbox.delete(0.0, "end")
    logs_textbox.delete(0.0, "end")
    
    try:
        resolved_ip = socket.gethostbyname(address)
        logs_textbox.insert("end", f"[*] Target resolved {address} => {resolved_ip}\n")
    except socket.gaierror:
        logs_textbox.insert("end", f"[!] Invalid IP or hostname: {address}\n")
        return

    first = int(first_entry)
    second = int(second_entry)

    if first < 1 or second > 65535 or first > second:
        logs_textbox.insert("end", "[!] Invalid port range\n")
        return

    total_ports = second - first + 1
    scanned_ports = 0

    for port in range(first, second + 1):
        if stop_event.is_set():
            logs_textbox.insert("end", "[!] Scan stopped by user\n")
            break
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(rate(rate_input))

        try:
            start_time = time.perf_counter()
            result = s.connect_ex((resolved_ip, port))
            end_time = time.perf_counter()

            calculated_time = end_time - start_time
            tcp_handshake_time = int(calculated_time * 1000)

            if result == 0:
                status = "OPEN"
                try:
                    banner = s.recv(1024)
                    if banner:
                        decoded_banner = banner.decode(errors = "ignore").strip()
                except socket.timeout:
                    decoded_banner = "(No banner)"
                except Exception as e:
                    decoded_banner = f"(Banner error: {e})"

                open_textbox.insert("end", f"[+] Port {port} | OPEN | RTT {tcp_handshake_time}ms\n")

            elif result in (111, 10061):
                status = "CLOSED"
                closed_textbox.insert("end", f"[-] Port {port} | CLOSED | RTT {tcp_handshake_time}ms\n")

            elif result in (110, 10060):
                status = "FILTERED / TIMEOUT"

                misc_textbox.insert("end", f"[?] Port {port} ... FILTERED / TIMEOUT | no reply\n")
            
            elif result in (11, 10035):
                status = "NO RESPONSE"
                misc_textbox.insert("end", f"[?] Port {port} ... NO RESPONSE | no reply\n")
            else:
                status = "ERROR"
                logs_textbox.insert("end", f"[!] Port {port} ... ERROR\n")
            
            logs_textbox.insert("end", f"[>] Scanning: Port {port}\n")
            logs_textbox.see("end")
            open_textbox.see("end")
            closed_textbox.see("end")
            misc_textbox.see("end")

            scanned_ports += 1
            progress = scanned_ports / total_ports
            progress_bar.set(progress)
            percentage_label.configure(text = f"{int(progress * 100)}%")
        finally:
            s.close()



