#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a server example which send hello to client.'

import time, socket, threading
import os



def tcplink(sock, addr):
    print ('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome!'.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        data = data.decode('utf-8')

        if data == 's' :

            sock.send('start'.encode('utf-8'))
            print('start')

            if os.path.exists("/home/nvidia/slam_end.txt"):
                os.system("rm /home/nvidia/slam_end.txt")

            os.system("./rgbd_rs ../../Vocabulary/ORBvoc.txt ./rs.yaml &")

            while True:

                if not os.path.exists("/home/nvidia/prepare_ready.txt"):
                    time.sleep(5)
                    print("wait...")

                else:

                    print("find it")

                    #os.system("rm /home/nvidia/prepare_ready.txt")

                    sock.send('ready'.encode('utf-8'))

                    print("find it")
                    print("find it")

                    break
                    

        elif data == 'q':

            sock.send('quit'.encode('utf-8'))
            print('quit')
            
            os.system("touch /home/nvidia/slam_end.txt")
        
            
        
    sock.close()
    print ('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('172.16.0.117', 12342))
s.listen(10) 
print ('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
