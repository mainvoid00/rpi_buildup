import socket
import time
import threading


# 송신측 IP 주소와 포트 번호
sender_ip = '169.254.186.47'
sender_port = 2222
video_file = './out.ts'
audio_file = './audio.mp3'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sender_ip, sender_port))
print("연결 완료:" ,sender_ip)


def recv_message():
    for i in range(300):
        data = s.recv(1024)
        message = data.decode()
        print("수신 메시지:", message)


def recv_video():
    # 동영상 파일 생성
    with open(video_file, 'wb') as file:
        # 소켓을 통해 전송된 데이터를 받아서 파일에 저장
        while True:
            

            block = s.recv(1024)  # 1024바이트씩 데이터 수신

            if not block:
                # 데이터 수신 완료
                file.seek(0)  # 파일 포인터를 다시 맨 처음으로 이동시킴

            file.write(block)  # 데이터를 파일에 저장

            break
    


def recv_audio():
    # 동영상 파일 생성
    with open(audio_file, 'wb') as file:
        # 소켓을 통해 전송된 데이터를 받아서 파일에 저장
        while True:
            

            block = s.recv(1024)  # 1024바이트씩 데이터 수신

            if not block:
                # 데이터 수신 완료
                file.seek(0)  # 파일 포인터를 다시 맨 처음으로 이동시킴

            file.write(block)  # 데이터를 파일에 저장

            break


thread_1 = threading.Thread(target=recv_message)
thread_2 = threading.Thread(target=recv_video)
thread_3 = threading.Thread(target=recv_audio)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()


s.close()