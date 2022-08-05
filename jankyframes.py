import subprocess
import time
from MyFile import *
from Util import *
import os.path
from datetime import datetime

def startJankyFrameTest():
 
  if isAdbConnected():
    subprocess.call("adb install -r myhapp1.apk")
    subprocess.call("adb shell input keyevent 26")
    subprocess.call("adb shell  input swipe 10 1000 10 10")
    #execute_adb("adb shell am instrument -w -m    -e package com.example.mhyapp -e debug false            #com.example.mhyapp.test/androidx.test.runner.AndroidJUnitRunner")
  else :
    print("device not detected")
    sys.exit()
    
  current_directory = os.getcwd()
  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  final_directory = os.path.join(current_directory, r'new_folder') 
  if not os.path.exists(final_directory):
    os.makedirs(final_directory)  

  #start the logs 
  #subprocess.call("adb logcat > jankframesalllogs.txt",shell=True)
   
  # start the apps which is required for janky frames data
  for app in range(len(allApps1)):
    print("starting all apps")
    packageapppp = allApps1[app].partition('/')
    
    #subprocess.call("adb shell monkey -p "+allApps[app]+" -c android.intent.category.LAUNCHER 1")
    print("starting app normally")
    subprocess.call("adb shell am start -n "+allApps1[app])
    time.sleep(5)
    print("reset normal")
    subprocess.call("adb shell dumpsys gfxinfo "+packageapppp[0] +" reset",shell=True)
    subprocess.call("adb shell dumpsys gfxinfo "+packageapppp[0] +" reset",shell=True)
    time.sleep(5)
    subprocess.call("adb shell input keyevent 4")
    time.sleep(1)
	
   #reset the gfx info and run the command and store it in file
   
  for r in range(len(allApps1)):
    count =0
    while count < 1:
      packageappp = allApps1[r].partition('/')
      
      print("start")
      print("reset before launcing")
      subprocess.call("adb shell dumpsys gfxinfo "+packageappp[0] +" reset",shell=True)
      subprocess.call("adb shell dumpsys gfxinfo "+packageappp[0] +" reset",shell=True)
      time.sleep(1)
      print("launching app..")
      subprocess.call("adb shell am start -n "+allApps1[r])
      #subprocess.call("adb shell monkey -p "+allApps[r]+" -c android.intent.category.LAUNCHER 1")
      time.sleep(5)
      count1=0
      while count1 <50:
          subprocess.call("adb shell  input swipe 10 1000 10 10 100")
          subprocess.call("adb shell  input swipe 10 1000 10 10 100")
          time.sleep(2)
          #packageappp = allApps[r].partition('/')
          #print("file gfxinfo")
          subprocess.call("adb shell dumpsys gfxinfo "+packageappp[0]+ ">>"+"new_folder/" +packageappp[0]+"jank.txt",shell=True)
          print("Flick #",count1)
          time.sleep(2)
          count1=count1+1
      print("Resetting gfx counter before next iteration...")
      subprocess.call("adb shell dumpsys gfxinfo "+packageappp[0] +" reset",shell=True)
      subprocess.call("adb shell dumpsys gfxinfo "+packageappp[0] +" reset",shell=True)
      time.sleep(2)
      subprocess.call("adb shell input keyevent 4")
      count = count+1
		