import telnetlib
import time
import camera
import switcher
import logging

print("Program Python sudah berjalan!")

logging.basicConfig(
    filename="your_log_file.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def open_telnet_connection(host, port):
    try:
        tn = telnetlib.Telnet(host, port, timeout=24 * 60 * 60)
        return tn
    except TimeoutError as e:
        print(f"Error: {e}")
        return None


def send_telnet_command(tn, command):
    tn.write(command.encode("utf-8") + b"\r\n")
    time.sleep(1)  # Tunggu sejenak untuk respons
    response = tn.read_very_eager().decode("utf-8")
    return response


def read_device_status(tn):
    packet = tn.read_until(b"\r\n")
    return packet


def main():
    telnet_host = "192.168.1.80"
    telnet_port = 23
    telnet_username = "clearone"
    telnet_password = "converge"

    while True:
        tn = open_telnet_connection(telnet_host, telnet_port)

        if tn is not None:
            try:
                # Autentikasi Telnet
                tn.read_until(b"Username: ")
                tn.write(telnet_username.encode("utf-8") + b"\r\n")
                tn.read_until(b"Password: ")
                tn.write(telnet_password.encode("utf-8") + b"\r\n")

                # Tunggu sejenak setelah autentikasi
                time.sleep(1)

                while True:
                    cp2_command = "beam 48T_1 9000 1"
                    response = send_telnet_command(tn, cp2_command)
                    print(response)

                    packet = read_device_status(tn)
                    print(packet.decode("UTF").rstrip("\n"))

                    print(len(packet))

                    slice = packet[27:-4].decode("UTF")
                    print(slice)
                    print(len(slice))
                    sliced_output = slice[2:]
                    print(sliced_output)
                    print(len(sliced_output))

                    if sliced_output == "000000000001":
                        print("Zona 1")
                        # Implementasi fungsi untuk Preset 1
                        preset1 = camera.preset1()
                        print(preset1)
                        # Implementasi memanggil preset switcher
                        input1 = switcher.preset1()
                        print(input1)
                        time.sleep(5)

                    elif sliced_output == "000000000010":
                        print("Zona 2")
                        # Implementasi fungsi untuk Preset 2
                        preset2 = camera.preset2()
                        print(preset2)
                        # Implementasi Memanggil Fungsi Preset switcher
                        input2 = switcher.preset2()
                        print(input2)
                        time.sleep(5)

                    elif sliced_output == "000000000100":
                        print("Zona 3")
                        # Implementasi fungsi untuk Preset 3
                        preset3 = camera.preset3()
                        input3 = switcher.preset3()
                        print(preset3)
                        print(input3)
                        time.sleep(5)

                    elif sliced_output == "000000001000":
                        print("Zona 4")
                        # Implementasi fungsi untuk Preset 4
                        preset4 = camera.preset4()
                        print(preset4)
                        time.sleep(5)

                    elif sliced_output == "000000010000":
                        print("Zona 5")
                        # Implementasi fungsi untuk Preset 5
                        preset5 = camera.preset5()
                        print(preset5)
                        time.sleep(5)
                    elif sliced_output == "000000100000":
                        print("Zona 6")
                        # Implementasi fungsi untuk Preset 6
                        preset6 = camera.preset6()
                        input6 = switcher.preset4()
                        print(preset6)
                        print(input6)
                    elif sliced_output == "000001000000":
                        print("Zona 7")
                        # Implementasi fungsi untuk Preset 7
                        preset7 = camera.preset7()
                        print(preset7)
                    elif sliced_output == "000010000000":
                        print("Zona 8")
                        # Implementasi fungsi untuk Preset 8
                        preset8 = camera.preset8()
                        print(preset8)
                    elif sliced_output == "000100000000":
                        print("Zona 9")
                        # Implementasi fungsi untuk Preset 9
                        preset9 = camera.preset9()
                        print(preset9)
                    elif sliced_output == "001000000000":
                        print("Zona 10")
                        # Implementasi fungsi untuk Preset 10
                        preset10 = camera.preset10()
                        print(preset10)
                    elif sliced_output == "010000000000":
                        print("Zona 11")
                        # Implementasi fungsi untuk Preset 11
                        preset11 = camera.preset11()
                        print(preset11)
                    elif sliced_output == "100000000000":
                        print("Zona 12")
                        # Implementasi fungsi untuk Preset 12
                        preset12 = camera.preset12()
                        print(preset12)

                    elif slice[2:-1] == "000000000000":
                        cp2_response = send_telnet_command(tn, cp2_command)
                        print(cp2_response)

                    else:
                        print("Tidak Ada Report")

                    time.sleep(1)  # Sleep for 1 second before checking again

            except Exception as e:
                print(f"Error: {e}")

            finally:
                tn.close()  # Tutup koneksi Telnet ketika selesai

        # Sleep before retrying the Telnet connection
        time.sleep(5)  # Sleep for 5 seconds before retrying


if __name__ == "__main__":
    main()
