#!/usr/bin/env python3

import os
import time
import uiautomator2

def pre_setting():
	try:
		os.system("adb shell input keyevent KEYCODE_WAKEUP")
		os.system("adb root")
		os.system("adb shell logcat -G 8MiB") # or adb shell logcat --buffer-size=8M, this cmd can set logger buffer to 8M but it need to be conducted every reboot
		os.system("adb shell am start -a com.android.setupwizard.FOUR_CORNER_EXIT") # skip OOBE page
		os.system("adb shell settings put global development_settings_enabled 1") # enable developer options
		os.system("adb shell settings put global stay_on_while_plugged_in 3") # enable stay awake
		os.system("adb shell settings put global bugreport_in_power_menu 1") # enable report shortcut
		os.system("adb shell settings put system screen_off_timeout 1800000") # set timmout to 30mins
		os.system("adb shell settings put secure clock_seconds 1") # enable seconds in clock
		#os.system("adb shell setenforce 0")
		#os.system("adb shell setprop gf.debug.dump_data 1") #old cmd, it's for enable image data
		#os.system("adb shell setprop vendor.gf.debug.dump_data 1") #old cmd, it's for enable image data
		#print("Enable FPS image capture")

	except:
		pass

def install_app():
	try:
		os.system("adb install /home/chiahaowu/Downloads/PY/System_UI_Tuner.apk && adb install /home/chiahaowu/Downloads/PY/deep_touch_demo.apk && adb install /home/chiahaowu/Downloads/PY/timememo.apk && adb install /home/chiahaowu/Downloads/PY/barometer.apk && adb install /home/chiahaowu/Downloads/PY/mulit_touch_test.apk")
		os.system("adb install /home/chiahaowu/Downloads/PY/GoogleMeet.apk && adb install /home/chiahaowu/Downloads/PY/spotify-8-7-48-1062.apk")
		os.system("python3 /home/chiahaowu/Downloads/PY/AndSysToolv1.7.6/install_AndSysTools.py")
	except:
		pass

def enable_touch():
	try:
		os.system("adb shell content insert --uri content://settings/system --bind name:s:show_touches --bind value:i:1") # enable show_touches
		os.system("adb shell content insert --uri content://settings/system --bind name:s:pointer_location --bind value:i:1") # enable pointer_location
	except:
		pass

def set_logger_buffer():
	d = uiautomator2.connect()
	os.system("adb shell am start -a android.settings.SETTINGS")
	time.sleep(0.5)
	while True:
		while True:
			if d(resourceId="com.android.settings:id/search_bar_title").exists():
				d(resourceId="com.android.settings:id/search_bar_title").click()
				break
			elif d(resourceId="com.android.settings:id/search_action_bar_title").exists():
				d(resourceId="com.android.settings:id/search_action_bar_title").click()
				break
		time.sleep(1.5)
		os.system("adb shell input text \"Logger\ buffer\ sizes\ \"")
		if d(resourceId="android:id/title", text="Logger buffer sizes").exists(timeout=5):
			time.sleep(1)
			d(resourceId="android:id/title", text="Logger buffer sizes").click()
			break
	if d(resourceId="android:id/title", text="Logger buffer sizes").exists(timeout=3):
		time.sleep(2)
		d(resourceId="android:id/title", text="Logger buffer sizes").click()
	time.sleep(0.5)
	d(resourceId="android:id/text1", text="8M").click()

def camera_format():
	os.system("adb shell input keyevent 3")
	time.sleep(1)
	os.system("adb shell am start -n com.google.android.GoogleCamera/com.android.camera.CameraLauncher")
	time.sleep(2)

	d = uiautomator2.connect()
	if d(text='Allow Camera to access this device’s location?').exists(timeout=10):
		d(text='While using the app').click()
	if d(text='Turned on by default').exists(timeout=10):
		d(text='Done').click()
	time.sleep(1)
	if d(resourceId="android:id/title", text="Photo Setting").exists(timeout=10):
		d(resourceId="android:id/title", text="Photo Setting").click()
	if d(text="More settings").exists(timeout=10):
		d(text="More settings").click()
	d(resourceId="android:id/title", text="Advanced").click()
	time.sleep(1)
	d(resourceId="android:id/title", text="Store videos efficiently").click()
	time.sleep(1)
	os.system("adb shell input keyevent 3")

pre_setting()
enable_touch()
install_app()
set_logger_buffer()
