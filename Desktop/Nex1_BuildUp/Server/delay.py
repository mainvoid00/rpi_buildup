
import os
import csv

def delay_collection(command):
    print(command)
    stream = os.popen(command)
    output = stream.read()
    output = output.split('\n')

    #ping 명령 마지막 줄
    rtt_line = len(output)-2

    #print("rtt 값")
    #print(output[rtt_line])
    #print('\n')

    #'='을 기준으로 rtt 값 분리
    rtt_list = output[rtt_line].split('=')

    rtt_name = rtt_list[0]
    rtt_data = rtt_list[1]

    #rtt_name에서 문자열 avg 추출
    rtt_name = rtt_name.split('/')
    avg_name = rtt_name[1]
    #print("rtt 'avg' 문자열 추출")
    #print(avg_name)
    #print('\n')

    #rtt_data에서 avg 값 추출
    rtt_data = rtt_data.split('/')
    avg_data = float(rtt_data[1])
    #print("rtt avg 값 추출")
    #print(avg_data)


    with open('./log/result/message.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([avg_data])

#delay_collection("ping 10.20.100.2 -c 10")
