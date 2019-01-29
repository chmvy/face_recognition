import socket
import re
import json
import base64,io
from PIL import Image
import time


def handle_request(client):
    rec_bytes = ''
    while True:
        rec_byte = client.recv(10240)
        rec_bytes += str(rec_byte, encoding='utf-8')
        if not rec_byte:
            break
    print(rec_bytes)
    matchObj = re.search('(\{.*\})',rec_bytes, re.M)
    recv_json = json.loads(matchObj.group())
    # if len(recv_json)==3:
    #     pass
    # elif len(recv_json)==5:
    #     print(rec_bytes)
    #     show_image(recv_json)
    #     show_time(recv_json)


    print(recv_json)
    print(len(recv_json))

def restart_facema(client):
    msg1 = bytes("HTTP/1.1 200 OK\r\n\r\n".encode())
    msg2 = bytes(str({
            "resultCode" :200,
            "deviceCode":"123134",
            "msg":"成功",
            "SyncState":1
            }).encode())
    client.send(msg1)
    client.send(msg2)

def setup_facema(client):
    msg1 = bytes("HTTP/1.1 200 OK\r\n\r\n".encode())
    msg2 = bytes(str({
        "resultCode": 200,
        "deviceCode": "123134",
        "msg": "成功",
        "SyncState": 3
    }).encode())
    client.send(msg1)
    client.send(msg2)



def show_image(file_json):
    # 显示图片
    in_img = file_json['InOutImg']
    in_img_binary = base64.b64decode(in_img)
    fiel_in = io.BytesIO(in_img_binary)
    image = Image.open(fiel_in)
    image.show()

def show_time(file_json):
    # 显示时间
    recv_time_mm = int(file_json['time'])
    recv_time_mm = int(file_json['time']) / 1000
    time_local = time.localtime(recv_time_mm)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    print(dt)

def update_person(time, client):
    # 更新人员信息
    time_now = int(time.time()) * 1000
    a = {
        "resultCode": 200,
        "aaData": [
            {
                "CustomerName": "李凌涛",
                "personId": "0023",
                "CardNO": "111",
                "CustomerIDNO": "484646464654646",
                "ModifyDate": 1536202008000,
                "Photo":
                    "\\SC-201811022118\share\01.jpg",
                "OPType": 1
            }
        ]
    }
    a["aaData"][0]["ModifyDate"] = time_now
    msg1 = bytes("HTTP/1.1 200 OK\r\n\r\n".encode())
    msg2 = bytes(str(a).encode())
    client.send(msg1)
    client.send(msg2)



def main():
    # 创建一个socket服务端
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = socket.gethostname()
    # print((host))
    s.bind(('192.168.3.126',9999))
    s.listen(5)
    # i = 1
    while True:
        c, addr = s.accept()
        handle_request(c)
        # print(addr)
        # restart_facema(c)
        # print("sucess")
        # update_person(time, c)
        # print("sucess")


if __name__ == "__main__":
    main()