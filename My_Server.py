import socket

HOST = ''
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 1024


while True:
  serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serv.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024)
  serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  serv.bind(ADDR)
  serv.listen(5)
  print ('listening ...')

  data ="hello from server"
  conn, addr = serv.accept()
  print ('client connected ... ', addr)
  #request=conn.recv(2048)
  #f=request
  f = "test_480p.mp4"
  file=open(f,"rb").read()
  print(len(file))
  #data=[file[i: i + 1024] for i in range(0, len(file), 1024)]
  
  j=0
  conn.send(file)
	
  print ('client disconnected')
  conn.close()
