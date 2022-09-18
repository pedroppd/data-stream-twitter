import socket, time;

PORT = 3003;
HOST = "localhost";

s = socket.socket();
s.connect((HOST, PORT));

while (True):
    data = s.recv(2048);
    print(data.decode("utf-8"));
    time.sleep(1);