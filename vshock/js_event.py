import struct


def emit(path, message):
    input_type = message['input_type']
    if input_type == 1:
        with open(path, 'wb') as stream:
            button_number = message['button_number']
            value = message['value']
            # data = bytearray([0, 0, 0, 0, value, 0, 1, button_number])
            data = struct.pack('8b', 0, 0, 0, 0, value, 0, 1, button_number)
            stream.write(data)
    elif input_type == 2:
        with open(path, 'wb') as stream:
            button_number = message['button_number']
            value = message['value']
            # data = bytearray([0, 0, 0, 0, 0, value, 2, button_number])
            data = struct.pack('8b', 0, 0, 0, 0, 0, value, 2, button_number)
            stream.write(data)
