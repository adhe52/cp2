import socket


def create_camera_socket(ip, port):
    camera_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    camera_socket.connect((ip, port))
    return camera_socket


def send_camera_command(camera_socket, command):
    camera_socket.send(command)
    response = camera_socket.recv(1024)  # Sesuaikan dengan kebutuhan
    return response


def close_camera_socket(camera_socket):
    camera_socket.close()


def preset1():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x01\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset2():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x02\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset3():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x03\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset4():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x04\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset5():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x05\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset6():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x06\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset7():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x07\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset8():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x08\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset9():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x09\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset10():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x10\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset11():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x11\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


def preset12():
    camera_socket = create_camera_socket(
        "192.168.1.180", 52381
    )  # Ganti dengan IP dan port kamera Anda
    command = b"\x01\x00\x00\x09\x00\x00\x00\x00\x81\x01\x04\x3F\x02\x12\xFF"
    response = send_camera_command(camera_socket, command)
    print(response)

    close_camera_socket(camera_socket)


# Implementasikan fungsi preset2, preset3, dan seterusnya dengan cara yang sama

# Contoh penggunaan
