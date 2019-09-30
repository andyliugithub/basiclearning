"""
# 1


password = input('Please input your password: ')

while "123456"!= password:
	password = input('Wroing password, please retry:')
else:
	print('Right')
"""
"""


# 2


import turtle

length = 50
step = 50
num = 0

while num < 8:
	print(num)
	num += 1

	turtle.penup()
	turtle.goto(length,length)
	turtle.pendown()
	turtle.goto(length * -1, length)
	turtle.goto(length * -1, length * -1)
	turtle.goto(length, length * -1)
	turtle.goto(length, length)
	length += step

else:
	print('Out', num)

turtle.done()
"""


# 3

"""
import turtle

length = 50
step = 50
num = 0

while num < 6:
	print(num)
	num += 1

	turtle.penup()
	turtle.goto(length * 2, length)
	turtle.pendown()
	turtle.goto(length * -2, length)
	turtle.goto(length * -2, length * -1)
	turtle.goto(length * 2, length * -1)
	turtle.goto(length * 2, length)
	length += step

else:
	print('out', num)

turtle.done()
"""


#4
"""
import random
startnum = random.randint(1,100)
num = eval(input('Please input your number:'))

while num != startnum:
	if num > startnum:
		print("big")
	else:
		print('small')
	num = eval(input('Please try your number again:'))

else:
	print('Right, the number is ', str(num),+'.','The random number is ', startnum)


"""

#5
"""
import os
cmd = input('cmd: ')
os.system(cmd)
"""

# 6

"""
import os

cmd = input('cmd: ')
while cmd!='quit':
	if cmd == "记事本":
		os.system('notepad')
	elif cmd == "进程":
		os.system('tasklist') 
	else:
		os.system('echo other')
	cmd = input('cmd:')
"""

# 7

"""
num = 1

while num < 100:
	print(num, end=" ")
	num += 1


for i in range(100):
	print(i)

"""

# 8


"""
for i in range(10):
	print(i, end=' ')
print("")

for i in range(2, 11, 2):
	print(i, end=" ")
print("")

for i in range(12, 1, -3):
	print(i, end=" ")
"""

# 9

"""
import time


starttime = time.time()
lastnum = 0
#num = 0

while num < 30000000:
	num += 1
	lastnum += num
#starttime = time.time()

for num in range(30000000):
	lastnum += num
print(lastnum)

endtime = time.time()
print(endtime - starttime)
"""

# 10 
"""
import time
import os

num = 0
while True:
	time.sleep(1)
	print('The' + str(num) + 'Sec')
	num +=1

	if num == 10:
		os.system('start notepad')
	elif num == 15:
		os.system('taskkill /f /im notepad.exe')
	elif num == 20:
		break
	else:
		pass


# 11 for_voice

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SPVOICE")

for i in range(5):
	speaker.Speak("I love Andy!")



# 12

for i in range(100):
	print(i, end=' ')
else:
	print('out', i)



# 13

for i in range(8):
	for j in range(6):
		print(j, end=' ')
	print('--------------', i)

"""

# 14

"""

import turtle


for i in range(0, 300, 100):

	for j in range(0, 400, 100):
		turtle.goto(j, i)
		turtle.pendown
		turtle.write(str(i) + ',' + str(j))
	turtle.penup()

turtle.done()


# 15

for i in range(10, 0, -2):
	print(i)


# 16

num = eval(input('Please input your number: '))

for i in range(100):
	if num == i:
		print('Find')
		break
	print(i)



# 17

for i in range(100):
	if i%2 == 0:
		continue
	print(i)



# 18

for i in range(8):
	
	if i == 5:
		continue
	print(i, end=' ')

	for j in range(6):
		if j == 3:
			continue
		print(j, end=' ')

	print('')


# 19

import win32con
import win32gui
import time

QQ = win32gui.FindWindow('TXGuiFoundation','QQ')
for num in range(10):
	time.sleep(0.5)
	if num%2 == 0:
		win32gui.ShowWindow(QQ,win32con.SW_HIDE)
	else:
		win32gui.ShowWindow(QQ,win32con.SW_SHOW)


# 20

import win32con
import win32gui
import time

notepad = win32gui.FindWindow('Notepad', '无标题 - 记事本')
for i in range(10):
	for size in range(0, 800, 10):
		win32gui.SetWindowPos(notepad, win32con.HWND_TOPMOST, 0, 0, size, size, win32con.SWP_SHOWWINDOW)

	for size in range(800, 0, -10):
		win32gui.SetWindowPos(notepad, win32con.HWND_TOPMOST, 0, 0, size, size, win32con.SWP_SHOWWINDOW)
"""

# 21


import win32con
import win32gui
import time


QQ = win32gui.FindWindow('TXGuiFoundation','QQ')

while True:
#	
	for size in range(0, 800, 10):
		win32gui.SetWindowPos(QQ, win32con.HWND_TOPMOST, size, size*768//1024, 900,
								 900, win32con.SWP_SHOWWINDOW)