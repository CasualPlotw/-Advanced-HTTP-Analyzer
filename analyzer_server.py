import socket
import threading
from datetime import datetime
import json

HOST = "127.0.0.1"
PORT = 8080

request_count = 0
path_stats = {}
blocked_paths = ["/admin"]
log_file = "logs.txt"

lock = threading.Lock()

def handle_client(client_socket, addr):
    global request_count

    request = client_socket.recv(1024).decode(errors="ignore")
    lines = request.split("\r\n")

    if not lines or len(lines[0].split()) < 3:
        client_socket.close()
        return

    method, path, version = lines[0].split()

    with lock:
        request_count += 1
        if path not in path_stats:
            path_stats[path] = 0
        path_stats[path] += 1

    log_entry = {
        "time": str(datetime.now()),
        "ip": addr[0],
        "method": method,
        "path": path
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"[{datetime.now()}] {addr[0]} -> {method} {path}")

    # Blocked path
    if path in blocked_paths:
        response_body = "<h1>403 Forbidden</h1><p>Bu sayfa engellendi.</p>"
        response = (
            "HTTP/1.1 403 Forbidden\r\n"
            "Content-Type: text/html\r\n\r\n"
            + response_body
        )
    elif path == "/stats":
        stats_html = "<h1>Server Stats</h1>"
        stats_html += f"<p>Total Requests: {request_count}</p><ul>"
        for p, count in path_stats.items():
            stats_html += f"<li>{p} : {count}</li>"
        stats_html += "</ul>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n\r\n"
            + stats_html
        )
    elif path == "/logs":
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                logs = f.read()
        except:
            logs = "No logs yet."

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n\r\n"
            + logs
        )
    else:
        response_body = f"<h1>Merhaba Mahir 😎</h1><p>Girdigin path: {path}</p>"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n\r\n"
            + response_body
        )

    client_socket.send(response.encode())
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Advanced Analyzer Server {HOST}:{PORT} calisiyor...")

while True:
    client_socket, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()