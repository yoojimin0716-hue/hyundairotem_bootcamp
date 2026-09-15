# 1회용 서버 
from socket import * 

# socket 객체 생성 
seversock = socket(AF_INET,SOCK_STREAM) #socket (소켓 종류, 소켓 유형) 
# socket을 이용해 특정 컴퓨터랑 바인딩 (서버의 IP와 PORT를 연결 )
seversock.bind(('192.168.0.44',8888))

# 연결 대기상태로 전환 
seversock.listen(5)
print('서버 서비스 중 ...')

# 클라이언트의 접속 대기 
conn, addr = seversock.accept() # 수동적으로 연결을 받음 
print('client addr : ',addr)

# 클라이언트가 보낸 데이터 수신 
msg = conn.recv(1024).decode()  # 1kb 단위로 수신된 데이터를 문자열로 변환
print('from client message : ',msg)

# 연결 종료 
conn.close()
seversock.close()