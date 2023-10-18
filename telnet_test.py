import telnetlib
import time

def send_telnet_command(host, port, command):
    try:
        # Koneksi ke device CP 2
        tn = telnetlib.Telnet(host, port, timeout=5)

        # Time Load
        time.sleep(1)

        #Status

        print(tn.read_very_eager().decode('ascii'))

        # kirim command
        tn.write(command.encode('ascii') + b"\r\n")

        #status Mesin
        response = tn.read_until(b"\r\n", timeout=2).decode('ascii')
        print(response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        #tutup koneksi
        tn.close()

cp2 =input("Masukan IP Address : ")
port = input(int("Masukan Port : "))

#Ambil status MEsin 
status_mesin = "Get 48T 1 0 1"

#kirim Perintah
send_telnet_command(cp2, port, status_mesin)

