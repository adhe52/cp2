import telnetlib


def send_telnet_command(ip_address, port, command):
    try:
        # Membuat koneksi Telnet
        tn = telnetlib.Telnet(ip_address, port, timeout=5)

        # Mengirim perintah ke switcher
        tn.write(command.encode("ascii") + b"\r\n")

        # Membaca dan mencetak hasil (opsional)
        result = tn.read_until(b"\r\n", timeout=5).decode("utf-8")
        print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Menutup koneksi Telnet
        tn.close()


def preset1():
    switcher_ip = "192.168.1.39"
    switcher_port = 5000
    switcher_command = "#VID 1>1"
    # Mengirim perintah Telnet
    send_telnet_command(switcher_ip, switcher_port, switcher_command)


def preset2():
    switcher_ip = "192.168.1.39"
    switcher_port = 5000
    switcher_command = "#VID 2>1"
    # Mengirim perintah Telnet
    send_telnet_command(switcher_ip, switcher_port, switcher_command)


def preset3():
    switcher_ip = "192.168.1.39"
    switcher_port = 5000
    switcher_command = "#VID 3>1"
    # Mengirim perintah Telnet
    send_telnet_command(switcher_ip, switcher_port, switcher_command)


def preset4():
    switcher_ip = "192.168.1.39"
    switcher_port = 5000
    switcher_command = "#VID 4>1"
    # Mengirim perintah Telnet
    send_telnet_command(switcher_ip, switcher_port, switcher_command)
