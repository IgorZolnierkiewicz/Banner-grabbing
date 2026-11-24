import socket
import sys

if len(sys.argv)>1:
    cel=sys.argv[1]
else:
    cel="127.0.0.1"

def skanuj_port(cel_ip, port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1.0)

    try:
        s.connect((cel_ip, port))
        print(f"[+] Sukces! Port {port} jest otwarty")
        try:
            baner = s.recv(1024)
        except socket.timeout:
            baner = b""
        if not baner:
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            try:
                baner=s.recv(1024)
            except socket.timeout:
                baner=b""
            
        tekst=baner.decode("utf-8", errors="ignore").strip()
        if tekst:
            pierwsza_linia=tekst.splitlines()[0]
            print(f"Odpowiedz: {pierwsza_linia}")            
        for linia in tekst.splitlines():
            if linia.lower().startswith("server:"):
                print(f"Wykryty baner: {linia}")
    except ConnectionRefusedError:
        print(f"[-] Port {port}: zamkniety (polaczenie odrzucone)")
    except socket.timeout:
        print(f"[-] Port {port}: brak odpowiedzi (timeout)")
    except OSError as e:
        print(f"[-] Port {port}: blad sieci ({e})")
    finally:
        s.close()
if len(sys.argv) > 2:
    porty_do_sprawdzenia = [int(sys.argv[2])]
else:
    porty_do_sprawdzenia = [21, 22, 80, 443, 8000, 8080]
print(f"[*] Rozpoczynam skanowanie {cel}...")
for p in porty_do_sprawdzenia:
    skanuj_port(cel,p)
print('[*] Skanowanie zakonczone')