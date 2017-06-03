import socket


HOST = ''
PORT = 8080
ADDR = (HOST, PORT)
BUFSIZE = 1024

last_seq = 0


def set_protocol(data):
    for i in range(0, len(data)):

        data[i] = bytes(set_seq(i), 'utf-8') + data[i]

    pass


def set_seq(i):
    if len(str(i)) == 1:
        return "0000" + str(i)
    if len(str(i)) == 2:
        return "000" + str(i)
    if len(str(i)) == 3:
        return "00" + str(i)
    if len(str(i)) == 4:
        return "0" + str(i)
    if len(str(i)) == 5:
        return str(i)
    pass


def get_seq(String):
	    #print(String[1],String[3])	
    return (String[1] + String[3] + String[5] + String[7] + String[9])


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serv.bind(ADDR)
serv.listen(5)


while True:
    print('listening ...')
    data = "hello from server"
    conn, addr = serv.accept()
    print('client connected ... ', addr)

    f = "test_144p.mp4"
    file = open(f, "rb").read()
    print(len(file))
    data = [file[i: i + 1019] for i in range(0, len(file), 1019)]
    j = 0
    print(len(data))
    set_protocol(data)
    next_seq = 0
    while j < len(data):

        conn.send(data[next_seq])
        print("waiting ",str(next_seq))
        try:
                print('attend recv....')
                request = conn.recv(1024).decode()	    
                print('apres recv....')
        except socket.timeout:
                
                #serv.bind(ADDR)
                #serv.listen(5)
                print('listening ...')
                data = "hello from server"
                conn, addr = serv.accept()
                print('client connected ... ', addr)
		

        next_seq = int(get_seq(request)) + 1

        last_seq = next_seq

        print(next_seq)
        j += 1

    print('client disconnected ...')
conn.close()

	
