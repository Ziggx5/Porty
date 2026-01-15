def probe_service(s, port):
    probes = {
        80: b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n",
        8000: b"GET /  HTTP/1.1\r\nHost: localhost\r\n\r\n",
        8080: b"GET /  HTTP/1.1\r\nHost: localhost\r\n\r\n",
        3000: b"GET /  HTTP/1.1\r\nHost: localhost\r\n\r\n",
        5000: b"GET /  HTTP/1.1\r\nHost: localhost\r\n\r\n",
        443: b"GET /  HTTP/1.1\r\nHost: localhost\r\n\r\n",
        21: b"QUIT\r\n",
        25: b"HELO test\r\n",
        587: b"HELO test\r\n",
        22: b"\r\n"
    }

    payload = probes.get(port, b"\r\n")

    try:
        s.sendall(payload)
        response = s.recv(1024)
        print(response)
        if response:
            text = response.decode(errors="ignore").strip()
            print(text)
            return "Guessed", text
    except TimeoutError:
        pass
    except Exception:
        pass

    return None, None