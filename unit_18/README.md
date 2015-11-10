# 21v-python

## Client

### Creating a socket

c1.py socket.socket function:

```
#Socket client example in python
 
import socket   #for sockets
 
#create an AF_INET, STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print 'Socket Created'
```

Функция socket.socket создает socket и возвращает socket descriptor, который может использоваться другой функцией

socket создается со свойствами


Address Family : AF_INET (это IP version 4 or IPv4)
Type : SOCK_STREAM (это соединение чвляется TCP)

## Error handling - перехват ошибок


```
#handling errors in python socket programs
 
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
```
## Работаем с сервером www.google.com

## Connect to a Server

Получим IP address и port для соединения. 

c3.py
```
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
```

python c3.py 
```
Socket Created
Ip address of www.google.com is 173.194.113.210
```
Выполним соединение на порт 80

```
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

```
python c4.py 
```
Socket Created
Ip address of www.google.com is 173.194.113.209
Socket Connected to www.google.com on ip 173.194.113.209
```
## Отсылаем данные на удаленный сервер

При соединении используем тип SOCK_STREAM/TCP сокета. 

## Sending Data

```
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'
```

python c5.py 
```
Socket Created
Ip address of www.google.com is 173.194.113.209
Socket Connected to www.google.com on ip 173.194.113.209
Message send successfully
```

## Receiving Data - Получение данных

## Function recv

```
#Socket client example in python
 
import socket   #for sockets
import sys  #for exit
 
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
     
print 'Socket Created'
 
host = 'www.google.com';
port = 80;
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    #Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'
 
#Now receive data
reply = s.recv(4096)
 
print reply
```
python c6.py 
```
Socket Created
Socket Connected to www.google.com on ip 173.194.113.209
Message send successfully
HTTP/1.1 302 Found
Cache-Control: private
Content-Type: text/html; charset=UTF-8
Location: http://www.google.com.ua/?gfe_rd=cr&ei=J-VBVt-dPM_A7gS2r4G4Bg
Content-Length: 262
Date: Tue, 10 Nov 2015 12:37:59 GMT
Server: GFE/2.0

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="http://www.google.com.ua/?gfe_rd=cr&amp;ei=J-VBVt-dPM_A7gS2r4G4Bg">here</A>.
</BODY></HTML>
```

## Close socket - закрываем соединение
```
s.close()
```
## Telnet
```
# telnet program example
import socket, select, string, sys
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host'
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print 'Connection closed'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
```

python telnet.py google.com 80
```
Connected to remote host

^]
HTTP/1.0 400 Bad Request
Content-Length: 54
Content-Type: text/html; charset=UTF-8
Date: Tue, 10 Nov 2015 13:37:11 GMT
Server: GFE/2.0

<html><title>Error 400 (Bad Request)!!1</title></html>Connection closed

```
## Connected to remote host
```
python telnet.py google.com 80
Connected to remote host
hello

HTTP/1.0 400 Bad Request
Content-Type: text/html; charset=UTF-8
Content-Length: 1555
Date: Tue, 10 Nov 2015 13:41:08 GMT
Server: GFE/2.0

<!DOCTYPE html>
<html lang=en>
  <meta charset=utf-8>
  <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
  <title>Error 400 (Bad Request)!!1</title>
  <style>
    *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}
  </style>
  <a href=//www.google.com/><span id=logo aria-label=Google></span></a>
  <p><b>400.</b> <ins>That’s an error.</ins>
  <p>Your client has issued a malformed or illegal request.  <ins>That’s all we know.</ins>
Connection closed

```
## Telnet Example

```
import getpass
import sys
import telnetlib

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
```

При использовании telnet в Python, при разрыве связи или закрытии сокета на удаленной стороне, telnet может не выдать ошибку закрытия соединения. Отловить разрыв соединения можно отправив NOP команду, ниже пример как можно определить разрыв соединения:
```
import telnetlib
import socket

try:
    tn = telnetlib.Telnet('google.com', 80)
    tn.write('GET / HTTP/1.0\n\n')
    while True:
        buf = tn.read_some()
        if buf:
            print buf
        else:
            tn.sock.sendall(telnetlib.IAC + telnetlib.NOP)
except socket.error:
    print 'connection was closed'
```
пример многопоточного скрипта для ping на Python при помощи модулей threading, Queue и subprocess. Если вам необходимо организовать взаимодействие с каждым процессом, то можно использовать функцию subprocess. Popen() в комплексе с потоками выполнения.
```
#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ["10.0.1.1", "10.0.1.3", "10.0.1.11", "10.0.1.51"]

def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()

for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

for ip in ips:
    queue.put(ip)

print "Main Thread Waiting"
queue.join()
print "Done"
```

многопоточный пинг позволяет сканировать большое количество ip (например 254) адресов за короткое время (5-20 секунд), тогда как у однопоточной версии на то же количество ip адресов уйдет порядка 12 минут.

импортируемые модули
- threading  
- Queue  
Каждый раз, когда вам требуется прибегнуть к использованию потоков, желательно использовать модуль Queue. Этот модуль снижает потребность в явной реализации защиты данных с помощью мьютексов, потому что внутренние механизмы механизмы самих очередей обеспечивают необходимую защиту данных.

Метод join() представляет собой простой способ предотвратить завершение выполнения главного потока программы до того, как остальные потоки выполнения получат шанс завершить обработку элементов очереди.


# Пишем socket servers

1. Открыть socket
2. Присоединиться к address(and port).
3. Слкшать incoming connections.
4. Принять connections
5. Read/Send


## socket

1.py
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

```
Проверка
```
telnet localhost 10000
```
## Function sendall
s1.py

```
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#wait to accept a connection - blocking call
conn, addr = s.accept()
 
print 'Connected with ' + addr[0] + ':' + str(addr[1])
 
#now keep talking with the client
data = conn.recv(1024)
conn.sendall(data)
 
conn.close()
s.close()
```
Проверка
```
telnet localhost 8888
```

## Live Server
ls1.py:
```
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data: 
        break
     
    conn.sendall(reply)
 
conn.close()
s.close()
```

telnet localhost 5000

## Handling Connections
ls2.py:
```
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
```
telnet localhost 8888


s2.py

```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
```

## Echo Client

```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
```
python c2.py 
```
connecting to localhost port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
closing socket
```

## Easy Client Connections
c3.py
```
import socket
import sys

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print >>sys.stderr, 'Family  :', families[sock.family]
print >>sys.stderr, 'Type    :', types[sock.type]
print >>sys.stderr, 'Protocol:', protocols[sock.proto]
print >>sys.stderr

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
```
python c3.py 
```
Family  : AF_INET
Type    : SOCK_STREAM
Protocol: IPPROTO_TCP

sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
closing socket
```

## Выбор адреса для прослушивания

s4.py
```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
```

python s4.py localhost

c4.py

```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    sock.close()
```
python c4.py localhost
```
connecting to localhost port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
```

# Сервер на 0.0.0.0
s5.py

```
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
```
python s5.py 
```
starting up on 0.0.0.0 port 10000
waiting for a connection
```
python c4.py localhost
```
connecting to localhost port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."
```

python c4.py 127.0.1.1
```
connecting to 127.0.1.1 port 10000
sending "This is the message.  It will be repeated."
received "This is the mess"
received "age.  It will be"
received " repeated."

```
server console
```
client connected: ('127.0.0.1', 45505)
received "This is the mess"
received "age.  It will be"
received " repeated."
received ""
waiting for a connection
client connected: ('127.0.0.1', 43340)
received "This is the mess"
received "age.  It will be"
received " repeated."
received ""
waiting for a connection

```
## BaseHTTPServer

### HTTP GET
http1.py 
```

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```

python http1.py 
```
Starting server, use <Ctrl-C> to stop
```
На другом терминале:
```
$ curl -i http://localhost:8080/?foo=barHTTP/1.0 200 OK
HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 09 Nov 2015 21:55:40 GMT

CLIENT VALUES:
client_address=('127.0.0.1', 45294) (localhost)
command=GET
path=/?foo=barHTTP/1.0
real path=/
query=foo=barHTTP/1.0
request_version=HTTP/1.1

SERVER VALUES:
server_version=BaseHTTP/0.3
sys_version=Python/2.7.6
protocol_version=HTTP/1.0

HEADERS RECEIVED:
accept=*/*
host=localhost:8080
user-agent=curl/7.35.0
curl: (7) Couldn't connect to server
curl: (6) Could not resolve host: OK

```
## HTTP POST

http2.py
```
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class PostHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')

        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
                        (field, field_item.filename, file_len))
            else:
                # Regular form value
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
python http2.py 
```
Starting server, use <Ctrl-C> to stop
```
Проверка 

```
curl http://localhost:8080/ -F name=dhellmann -F foo=bar -F  datafile=@http2.py
Client: ('127.0.0.1', 45312)
User-agent: curl/7.35.0
Path: /
Form data:
    Uploaded datafile as "http2.py" (1567 bytes)
    foo=bar
    name=dhellmann


```
## Threading и Forking


```
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
Each time a request comes in, a new thread or process is created to handle it:
```
$ curl http://localhost:8080/
Thread-1
$ curl http://localhost:8080/
Thread-2
$ curl http://localhost:8080/
Thread-3


Starting server, use <Ctrl-C> to stop
127.0.0.1 - - [10/Nov/2015 00:02:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Nov/2015 00:02:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Nov/2015 00:02:29] "GET / HTTP/1.1" 200 -

```

## Handling Errors - перехват ошибок send_error(). 

http4.py
```
from BaseHTTPServer import BaseHTTPRequestHandler

class ErrorHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_error(404)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
## curl
```
curl -i http://localhost:8080/
HTTP/1.0 404 Not Found
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 09 Nov 2015 22:05:15 GMT
Content-Type: text/html
Connection: close

<head>
<title>Error response</title>
</head>
<body>
<h1>Error response</h1>
<p>Error code 404.
<p>Message: Not Found.
<p>Error code explanation: 404 = Nothing matches the given URI.
</body>


Starting server, use <Ctrl-C> to stop
127.0.0.1 - - [10/Nov/2015 00:04:55] code 404, message Not Found
127.0.0.1 - - [10/Nov/2015 00:04:55] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [10/Nov/2015 00:05:15] code 404, message Not Found
127.0.0.1 - - [10/Nov/2015 00:05:15] "GET / HTTP/1.1" 404 -

```
## Setting Headers - установка заголовка - send_header method 

http5.py

```
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import time

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Last-Modified', self.date_time_string(time.time()))
        self.end_headers()
        self.wfile.write('Response body\n')
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
```
Устанавливаем заголовок Last-Modified согласно RFC 2822.
```
curl -i http://localhost:8080/
HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 09 Nov 2015 22:08:32 GMT
Last-Modified: Mon, 09 Nov 2015 22:08:32 GMT

Response body

Starting server, use <Ctrl-C> to stop
127.0.0.1 - - [10/Nov/2015 00:08:32] "GET / HTTP/1.1" 200 -

```
