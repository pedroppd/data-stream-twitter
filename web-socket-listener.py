import socket, time, os
from model.twitter import Twitter;

PORT = 3003;
HOST = "localhost";
CONNECTION_NUMBER = 5;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.bind((HOST, PORT));
print(f'Loading connection from socket {HOST} to port {PORT} ...');

s.listen(CONNECTION_NUMBER);
conn, address = s.accept();
print(f'Connection established: {address}');
token = '';
tweets = Twitter(conn, token);
printer = tweets.on_tweet();
conn.close();