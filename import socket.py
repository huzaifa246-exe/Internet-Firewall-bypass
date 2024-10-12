import socket

def is_internet_accessible():
    try:
        # Try to connect to a well-known DNS server (Google's)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

if is_internet_accessible():
    print("Internet access is available.")
else:
    print("No internet access or blocked by firewall.")
