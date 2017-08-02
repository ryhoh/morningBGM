# -*- coding: utf-8 -*-

import subprocess
import datetime
import RPi.GPIO as GPIO

# 再生用コマンド
command = "mpg321 -g 100 "

# 制御用スイッチの番号
switch = 27

# 曜日ごとに鳴らす時刻（時）を整数で指定
# [添字] : 月曜-日曜の時刻
ringHour = [7, 7, 7, 7, 7, 7, 8]

# 曜日ごとに鳴らすBGMのファイル名を指定
# パス、拡張子は含まないこと
music = [[42, 43], [44, 45], [46, 47], [18, 19], [32, 33], [26, 27], [54, 55]]

# BGMファイルのパス（cronで呼び出せるよう絶対パスで指定）
musicPathPart = "/home/pi/nas/librarian_bgm/0000"
pathOpening = "/home/pi/nas/Maid_with_the_Flaxen_Hair.mp3"


################################################################################################

# イントロとメインで別ファイルになっている、ループする音楽の場合
def play(musicIntro, musicMain):
	intro = musicPathPart + str(musicIntro) + ".mp3"
	main = musicPathPart + str(musicMain) + ".mp3"
	
	# オープニングBGMを1回流す
	if GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + pathOpening, shell=True)
	
	# 通常BGMはスイッチが入っている限り鳴り続ける
	if GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + intro, shell=True)
	while GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + main, shell=True)

"""
# 単独ファイルの音楽の場合
def play(music):
	main = musicPathPart + str(music) + ".mp3"
	
	# オープニングBGMを1回流す
	if GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + pathOpening, shell=True)
	
	# 通常BGMはスイッチが入っている限り鳴り続ける
	while GPIO.input(switch) == GPIO.LOW:
		subprocess.call(command + main, shell=True)
"""

################################################################################################

# gpio初期化
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)	# 入力にセット

today = datetime.datetime.now()

# 曜日：月曜日を0として整数で扱う
weekday = today.weekday()
# 時刻：24時間で表す
hour = today.hour

# 鳴らすかどうか判断
if hour == ringHour[weekday]:
	play(*music[weekday])

#print str(weekday) + " " + str(hour)

