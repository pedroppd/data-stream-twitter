import socket, time

PORT = 3000;
HOST = "localhost";
CONNECTION_NUMBER = 5;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.bind((HOST, PORT));
print(f'Loading connection from socket {HOST} to port {PORT} ...');

s.listen(CONNECTION_NUMBER);
conn, address = s.accept();
print(f'Connection established: {address}');

messages = [
        "teste webSocket 1", 
       "Teste webSocket 2", 
       "Teste webSocket 3", 
       "Teste webSocket 4", 
       "Teste webSocket 5", 
       "Teste webSocket 6", 
       "Teste webSocket 7"];

for message in messages:
    byteMessage = bytes(message, "utf-8");
    conn.send(byteMessage);
    time.sleep(1);

conn.close();