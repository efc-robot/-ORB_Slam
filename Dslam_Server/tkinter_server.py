#!/usr/bin/env python
# coding=utf8

from socket import *
import os
import subprocess
import time


os.system("source /opt/ros/jade/setup.bash")


host = '172.16.0.104'  # TODO 替换成服务器IP
port = 12349
bufsiz = 1024

wait_time = 5




tcpSerSock_2 = socket(AF_INET, SOCK_STREAM)   # 开启套接字
tcpSerSock_2.bind((host, port))               # 绑定服务端口
tcpSerSock_2.listen(5)                        # 开始监听

while True:
	print ('Please waiting for connection...')      # 等待客户端连接
	tcpCliSock_2, addr = tcpSerSock_2.accept()		  # 接受连接
	print ('...connected from:', addr)


	data = tcpCliSock_2.recv(bufsiz)      # 接收客户端信息
	if not data:
	    break
	return_data = "Hello client, I am server. connect successfully!"
	tcpCliSock_2.send(return_data)    # 给客户端发送信息

#TODO
	if data == 'open vrpn'

'''
	while True:

		response = tcpCliSock_2.recv(bufsiz)
		response = response.decode('utf-8')

		if response == 'open vrpn':
			break
		else:
			print (response)
			time.sleep(2)
'''
		
	# 异步调用
	print("one")
	subprocess.Popen("roslaunch vrpn_client_ros sample.launch server:=172.16.0.105 >> start_ros.txt", shell=True)
	print("start_ros")

	time.sleep(20)

	print("two")
	# 获取位置信息
	os.system("rostopic echo /vrpn_client_node/RigidBody01/pose > pos.txt &")
	print("three")
	#客户端发送结束指令，服务端接收kill指令
	

	if response == 'kill':
		
#杀死pose进程，执行format conversion
	os.system("ps aux | grep rostopic > ps_aux_grep.txt")

	while True:
		if not os.path.exists("ps_aux_grep.txt"):
			time.sleep(5)
		else:
			with open ("ps_aux_grep.txt", "r") as fr:   #fr = open("ps.txt","r")

				ps_aux_grep_contents = fr.read
				ps_name = "echo /vrpn_client_node/RigidBody01/pose"
				if ps_name in ps_aux_grep_contents:

					tt = ps_aux_grep_contents.split('')

					kill = "kill -9 " + tt[3] 

					print(kill)

					os.system(kill)

					break
				else:
					time.sleep(5)

	

	os.system("python format_conversion.py")
	
#检验刚体创建是否成功
'''
	while True:
		if not os.path.exists("start_ros.txt"):
			time.sleep(wait_time)
		else:
			with open("start_ros.txt", 'r') as fr:
				contents = fr.read()
				create_new_tracker = "Creating new tracker"
				if create_new_tracker in contents:
					#print（"create tracker successfully!"）
					break
				else:
					time.sleep(wait_time)
'''

'''
	# TODO
	require_from_client = tcpCliSock_2.recv(bufsiz)
	print (require_from_client)

	with open("pos.txt", 'r') as fr:
		pos_contents = fr.read()
		print ('pos data: ', pos_contents)
		tcpCliSock_2.send(pos_contents)

	tcpCliSock_2.close()
'''
tcpSerSock_2.close()
