# -*- coding: utf-8 -*-

import subprocess
import datetime
import RPi.GPIO as GPIO

# 鳴らす音楽（絶対パスで指定）
command = "mpg321 -g 100 "
pathOpening = "/home/pi/nas/Maid_with_the_Flaxen_Hair.mp3"
pathBGM = "/home/pi/nas/librarian_bgm/000029.mp3"

switch = 27

# gpio初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)	# 入力にセット

def play():
	# オープニングBGMを1回流す
	if GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + pathOpening, shell=True)
	# 通常BGMはスイッチが入っている限り鳴り続ける
	while GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + pathBGM, shell=True)
	
	#while GPIO.input(switch) == GPIO.LOW:
    #    	subprocess.call("python /home/pi/code/audioPlayer/audioPlayer.py", shell=True)


today = datetime.datetime.now()

# 曜日：月曜日を0として整数で扱う
weekday = today.weekday()
# 時刻：24時間で表す
hour = today.hour

# 朝6時に起きる曜日
from6 = [1, 2, 4]
# 朝7時30分に起きる曜日
from7 = [0, 3]

# 鳴らすかどうか判断
if hour is 6:
	for i in from6:
		if i is weekday:
			play()
if hour is 7:
	for i in from7:
		if i is weekday:
			play()


#print str(weekday) + " " + str(hour)

