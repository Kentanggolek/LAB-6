import socket


ClientSocket = socket.socket()
host = '192.168.56.107'
port = 8888

print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

while True:

	status = 0
	while(status == 0):
		option = input(' Enter type of operation (log || sqrt || exp): ')
		if(option == 'log'):
			val = input(" Enter the value: ")
			status = 1
		elif(option == 'sqrt'):
			val = input(" Enter the value: ")
			status = 1
		elif(option == 'exp'):
			val = input(" Enter the value: ")
			status = 1
		else:
			print(" Invalid input, please re-enter..")
			status = 0


	Input = option + " " +  val
	ClientSocket.send(str.encode(Input))
	Response = ClientSocket.recv(1024)
	print(Response.decode('utf-8'))
	print("\n")

ClientSocket.close()
