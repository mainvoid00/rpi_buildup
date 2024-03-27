
import threading
import os
import socket
import delay
import time

HOST = '0.0.0.0'
PORT = 2222
message= "Hello this is test"
video_file = "./output.ts"
audio_file = "./audio.mp3"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print("수신 대기 중...")
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)


def send_message_func():
    
    for i in range(300):
        conn.send(message.encode())
        time.sleep(0.1)
    print("메시지 전송 완료")
    


def send_video_func():
    for i in range(300):

        with open(video_file, 'rb') as file:
            # 파일 데이터를 작은 블록으로 나누어 전송
            while True:
                # 중지 이벤트가 설정되면 전송 중단
                #if stop_event.is_set():
                #    break

                block = file.read(1024)  # 1024바이트씩 읽기

                if not block:
                    # 파일 전송 완료
                    file.seek(0)  # 파일 포인터를 다시 맨 처음으로 이동시킴
                
                # 데이터 전송
                conn.sendall(block)
                print("비디오 전송 완료")
                break
    

def send_audio_func():
    for i in range(300):

        with open(audio_file, 'rb') as file:

            while True:
                block = file.read(1024)

                conn.sendall(block)
                print("오디오 전송 완료")
                break



#thread_1=threading.Thread(target=delay.delay_collection, args= ("ping 169.254.178.230 -c 300",))
thread_2= threading.Thread(target=send_message_func)
thread_3 = threading.Thread(target= send_audio_func)
thread_4 = threading.Thread(target=send_audio_func)
#thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_2.join()
thread_3.join()
thread_4.join()

conn.close()
s.close()
