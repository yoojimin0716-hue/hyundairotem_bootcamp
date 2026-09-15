# client 
from socket import * 

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.44',7788)) #사이트의 고유한 내용을 알수있게해주는 코드 : 8888
clientsock.send('반가워'.encode()) # 문자열을 바이트로 변환해서 서버로 전환
print('수신 자료 : ',clientsock.recv(1024).decode())

clientsock.close()

#server 실행중 - client 실행 - server가 메세지 수신 후 종료 