# client 
from socket import * 

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.44',8888)) #사이트의 고유한 내용을 알수있게해주는 코드 : 8888
clientsock.send('안녕 서버'.encode())

clientsock.close()

#server 실행중 - client 실행 - server가 메세지 수신 후 종료 