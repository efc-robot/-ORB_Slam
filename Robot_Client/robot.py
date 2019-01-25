#!/usr/bin/env python
# coding=utf8

import tkinter as tk
from socket import *
import time
import click


window = tk.Tk()
window.title('robot platform')
window.geometry('800x500')


l = tk.Label(window, text='Welcome to My Robot Platform !', bg='yellow', font=('Arial',20),
	width=60, height=4)
l.pack()

#user information

tk.Label(window, text='User name:', font=('Arial',14),
	width=8).place(x=200, y=120)
tk.Label(window, text='Password:', font=('Arial',14),
	width=8).place(x=200, y=160)

var_usr_name = tk.StringVar()
var_usr_name.set('example@robot.com')
enty_usr_name = tk.Entry(window, textvariable=var_usr_name).place(x=300, y=120)

var_usr_pwd = tk.StringVar()
enty_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*').place(x=300, y=160)


def usr_login():
	usr_name = var_usr_name.get()
	usr_pwd = var_usr_pwd.get()
	try:
		with open('usrs_info.pickle','rb') as usr_file:
			usrs_info = pickle.load(usr_file)
	except FileNotFoundError:
		with open('usrs_info.pickle','wb') as usr_file:
			usrs_info = {'admin':'admin'}
			pickle.dump(usr_info,usr_file)

	if usr_name in usrs_info:
		if usr_pwd == usrs_info[usr_name]:
			tk.messagebox.showinfo(title='Welcome', message='How are you?' + usr_name)
		else:
			tk.messagebox.showerror(message='Error, your password is wrong, please try again.')
	else:
		is_sign_up = tk.messagebox.askyesno(title='Welcome', message='you have not sign up yet. Sign up today?')
		if is_sign_up:
			usr_sign_up()


def usr_sign_up():
	def sign_to_Mofan_Python():
		np = new_pwd.get()
		npf = new_pwd_confirm.get()
		nn = new_name.get()
		with open('usrs_info.pickle','rb') as usr_file:
			exist_usr_info = pickle.load(usr_file)
		if np != npf:
			tk.messagebox.showerror(title='Error', text='Password and confirm Password must be the same!')
		elif nn in exist_usr_info:
			tk.messagebox.showerror(title='Error', text='The user has already signed up!')
		else:
			exist_usr_info[nn] = np
			with open ('usrs_info.pickle','wb') as usr_file:
				pickle.dump(exist_usr_info, usr_file)
			tk.messagebox.showiinfo(title='Welecome',text='You have successfully sign up!')
			window_sign_up.destroy()




	window_sign_up = tk.Toplevel(window)
	window_sign_up.geometry('350x200')
	window_sign_up.title('Sign up window')


	new_name = tk.StringVar()
	new_name.set('example@robot.com')
	tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
	entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
	entry_new_name.place(x=150, y=10)


	new_pwd = tk.StringVar()
	tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
	enty_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
	enty_usr_pwd.place(x=150, y=50)


	new_pwd_confirm = tk.StringVar()
	tk.Label(window_sign_up, text='Confirm Password:').place(x=10, y=90)
	entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
	entry_usr_pwd_confirm.place(x=150, y=90)


	btn_confirm_sign_up = tk.Button(window_sign_up,text='Sign up', command=sign_to_Mofan_Python)
	btn_confirm_sign_up.place(x=150, y=130)


#login and sign up button

btn_login = tk.Button(window, text='Login', command=usr_login).place(x=300, y=200)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up).place(x=400, y=200)



#Function Button

tcpCliSock_1 = socket(AF_INET, SOCK_STREAM)

def connect_tx1_server():
	host = '172.16.0.117'
	port = 12344
	bufsiz = 10240
    # 开启套接字
	tcpCliSock_1.connect((host, port))             # 连接到服务器
	print("start listening...")
	

tcpCliSock_2 = socket(AF_INET, SOCK_STREAM)

def connect_optitrack_server():
	host = '172.16.0.104'
	port = 12349
	bufsiz = 10240

	    # 开启套接字
	tcpCliSock_2.connect((host, port))             # 连接到服务器
	while True:
		data = "Hello server. I am client."
		tcpCliSock_2.send(bytes(data, encoding = "utf8"))       # 发送信息
		response = tcpCliSock_2.recv(bufsiz)       # 接受返回信息
		if not response:
		    break

		print (response)

		break
'''
	tcpCliSock_2.send(bytes("require pos data...", encoding = "utf8"))

	pos_info = tcpCliSock_2.recv(bufsiz)
	if pos_info:
		print (pos_info)
 
	tcpCliSock_2.close()
'''

b = tk.Button(window, text='connect tx1', command = connect_tx1_server, width=9,
	height=2,font=('Arial',18)).place(x=150,y=350)

b = tk.Button(window, text='connect opt', command = connect_optitrack_server, width=9,
	height=2,font=('Arial',18)).place(x=270,y=350)

b = tk.Button(window, text='recorded', width=9,
	height=2,font=('Arial',18)).place(x=390,y=350)

b = tk.Button(window, text='save', width=9,
	height=2,font=('Arial',18)).place(x=510,y=350)




def ORB_SLAM():
	bufsiz = 10240


	tcpCliSock_1.send('s'.encode('utf-8'))
	

	while True:

		response = tcpCliSock_1.recv(bufsiz)
		response = response.decode('utf-8')
		
		print("Qwer" + response)

		if response == 'start':
			break
		else:
			print( "Qwer1" + response)
			time.sleep(2)

	while True:

		response = tcpCliSock_1.recv(bufsiz)       # 接受返回信息
		response = response.decode('utf-8')

		if response == 'ready':
			break

		else:
			print (response)
			time.sleep(2)
	print('s')

	tcpCliSock_2.send(bytes("open vrpn", encoding = "utf8"))
	tcpCliSock_2.close()
'''
	#接受结束信息
	while True:

		response = tcpCliSock_1.recv(bufsiz)       
		response = response.decode('utf-8')

		if response == 'qiut':
			break

		else:
			print (response)
			time.sleep(2)

	tcpCliSock_2.send(bytes("end", encoding = "utf8"))
	'''

	

'''
	tcpCliSock_2.send(bytes("require pos data...", encoding = "utf8"))

	pos_info = tcpCliSock_2.recv(bufsiz)
	if pos_info:
		print (pos_info)
 '''




def Quit_SLAM():
	tcpCliSock_1.send('q'.encode('utf-8'))
	print('q')
	tcpCliSock_2.send("kill".encode('utf-8'))
	print("kill")


b = tk.Button(window, text='ORB_SLAM', command=ORB_SLAM, width=11,
	height=2,font=('Arial',18)).place(x=630,y=350)

b = tk.Button(window, text='Quit_SLAM', command=Quit_SLAM, width=11,
	height=2,font=('Arial',18)).place(x=630,y=400)



#car control
b = tk.Button(window, text='W', width=4,
	font=('Arial',18)).place(x=330,y=390)
b = tk.Button(window, text='A', width=4,
	font=('Arial',18)).place(x=260,y=420)
b = tk.Button(window, text='S', width=4,
	font=('Arial',18)).place(x=330,y=420)
b = tk.Button(window, text='D', width=4,
	font=('Arial',18)).place(x=400,y=420)



#car selection

var1 = tk.StringVar()
l = tk.Label(window, bg='green', width=4,
	textvariable=var1).place(x=200,y=220)

def print_selection():
	global lb
	global var1
	value = lb.get(lb.curselection())
	var1.set(value)

b1 = tk.Button(window,text='car selection', width=10,
		height=2, font=('Arial',18), command=print_selection).place(x=200,y=240)


var2 = tk.StringVar()
var2.set(('car 1', 'car 2', 'car 3', 'car 4'))
lb = tk.Listbox(window, width=5, height=4, listvariable=var2).place(x=200,y=280)

var3 = tk.StringVar()
var3.set('Camera')
lb = tk.Listbox(window, width=15, height=5, listvariable=var3, font=('Arial',18)).place(x=350,y=240)

var4 = tk.StringVar()
var4.set('IMU')
lb = tk.Listbox(window, width=15, height=5, listvariable=var4, font=('Arial',18)).place(x=530,y=240)

window.mainloop()

