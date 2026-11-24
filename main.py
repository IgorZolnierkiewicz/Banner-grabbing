import socket

cel_ip="127.0.0.1"
port=8000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2.0)

try:
    print(f"[*] Probuje polaczyc sie z {cel_ip}:{port}...")
    s.connect((cel_ip, port))
    print("[+] Sukces! Port jest otwarty")
    zapytanie=b"HEAD / HTTP/1.0\r\n\r\n"
    s.sendall(zapytanie)
    odpowiedz=s.recv(1024).decode("utf-8", errors="ignore")
    print("[+] Odpowiedz serwera: ")
    print(odpowiedz)
except ConnectionRefusedError:
    print("[-] Polaczenie odrzucone (port zamkniety)")
finally:
    s.close()