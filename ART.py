import subprocess
import threading
import time
from Util import *
from MyFile import *
from jankyframes import *
import sys


def execute_adb(command):
  subprocess.call(command,shell=True)

def forceStopPackage(packageName):
  #execute_adb("adb shell pm clear "+packageName)  
  execute_adb("adb shell am force-stop "+packageName)  
  
def runAllLog():
  thlog = threading.Thread(target=takeLogs)
  thlog.start()
  
def takeLogs(): 
  try:
      execute_adb("adb logcat -c")
      execute_adb("adb logcat > "+getFileName()+".txt")
  except (KeyboardInterrupt, SystemExit):
     sys.exit() 

def warmLaunch():
  runAllLog()
  print("performance selected")
  #print("Checking if device is selected")
  
  #apps = ['com.android.settings','com.android.dialer'] #,'com.android.dialer','com.android.gallery3d','com.google.android.gm.lite']
  for r in range(len(allApps)):
    forceStopPackage(allApps[r])
      #execute_adb("adb devices")
  adbUp()
  for app in range(len(allApps)):
    execute_adb("adb shell am start -n "+allApps[app])
    #execute_adb("adb shell monkey -p "+allApps[app]+" -c android.intent.category.LAUNCHER 1")
    time.sleep(5)
   # while not getBack:
   #   time.sleep(1)
      
    print("wake")
   # setBack(False)
    execute_adb("adb shell input keyevent 4")
    time.sleep(1)
  time.sleep(5)
  execute_adb("adb logcat -c")  
  execute_adb("adb logcat -c");
  # start the logs here in a seperate thread so that main therad which launches the app is nto blocked otherwise
  # it will be a deadlock sitaition
  th = threading.Thread(target=readLogsInSeperateThread)
  th.start()
  setShouldLogRun(True)
  count = 0
  for i in range(len(allApps)):
    count = 0
    while count<1:
      #setBack(False)
      #execute_adb("adb shell monkey -p "+allApps[i]+" -c android.intent.category.LAUNCHER 1")
      execute_adb("adb shell am start -n "+allApps[i])
      time.sleep(10)
      execute_adb("adb logcat -b all -c")
      # launhch app anhd get back
      #while not getBack():
      # print("still not displayed ")
       #time.sleep(1)
      #print("dispalyed")       
      execute_adb("adb shell input keyevent 4")
      time.sleep(2)
      #setBack(False)
      #wait for sometime , what id system is thrashing and it takes time
      count = count+1
      time.sleep(2)
      print("Launching again...",count,"interations done ..")
    
  print("Test complete for ",allApps[i])  
  setShouldLogRun(False)
  print("*********************************************************************************************\n\n")
  print("press ctrl c ")
  #input("Press Enter to Quit.....");


########################### Cold launch procedure ############################################################

def coldLaunch():
  #execute_adb("adb shell dumpsys activity | findstr realActivity")
  runAllLog()
  MAX_LOOP_COUNT=int(getCountEachApp())
  print("Each App will run [",MAX_LOOP_COUNT,"times ]\n")
  if (MAX_LOOP_COUNT>1):
    setMultiRuninLoop(1)
  else:
    setMultiRuninLoop(0)
  
  adbUp()
  #apps = ['com.android.settings','com.android.dialer'] #,'com.android.dialer','com.android.gallery3d','com.google.android.gm.lite']
  for r in range(len(allApps)):
    #forceStopPackage(allApps[r])
    packageappp = allApps[r].partition('/')  
    #forceStopPackage(allApps[i])
    forceStopPackage(packageappp[0])
    #execute_adb("adb devices")
  
  #f
  execute_adb("adb logcat -c")  
  execute_adb("adb logcat -c");
  # start the logs here in a seperate thread so that main therad which launches the app is nto blocked otherwise
  # it will be a deadlock sitaition
  th = threading.Thread(target=readLogsInSeperateThread)
  th.start()
  setShouldLogRun(True)
  count = 0
  matches =["facebook","instagram","whatsapp","amazon","youtube","gaana","paytm","olacabs","truecaller"]
  for i in range(len(allApps)):
    count = 0
    print("\n\n##############################################################################################\n")
    while count < MAX_LOOP_COUNT:
      #execute_adb("adb shell monkey -p "+allApps[i]+" -c android.intent.category.LAUNCHER 1")
      execute_adb("adb shell am start -n "+allApps[i])
      packageapp = allApps[i].partition('/')
      setlastPackageLoaded(allApps[i].split("/")[-1],packageapp[0])
      time.sleep(5)
      execute_adb("adb logcat -b all -c")
      #setlastPackageLoaded()
      
      #print("pushed activity after launch..",allApps[i].split("/")[-1])
      # launhch app anhd get back 
      
      time.sleep(1)
      execute_adb("adb logcat -c");

      
      #forceStopPackage(allApps[i])
      forceStopPackage(packageapp[0])
      #print(packageapp)
      

      #print("Removing package [",packageapp[0],"]")
        
      #wait for sometime , what id system is thrashing and it takes time
      count = count+1
      time.sleep(2)
      
      subprocess.Popen(['adb', 'shell', 'ps'], stdout=subprocess.PIPE, text=True) #universal_newlines=True)
      proc = subprocess.Popen(['adb', 'shell', 'ps'], stdout=subprocess.PIPE, universal_newlines=True, errors='ignore')
      for lin in proc.stdout:
        if any (x in lin for x in matches):
            l=lin.split()
            #print(l[8])
            execute_adb("adb shell am force-stop "+l[8])
            #print("cleared package ",l[8],"...")
        
    #execute_adb("adb shell pm clear "+packageapp[0])
    
  
  setShouldLogRun(False)
  
  print("*******************************************************************\n\n")
  print("press ctrl c ") 
  
def jankyFrames():
  print("Janky framses")
  # run the commands and put them in file and read from there..
  
def startMonkeyTest():
  runAllLog()
  execute_adb("adb shell monkey --ignore-crashes --ignore-timeouts --ignore-security-exceptions 505555")
  
  
  
def adbUp():
  #print("Checking if device is selected")
     #execute_adb("adb devices")
  if isAdbConnected():
    #execute_adb("adb install -r C:\\Users\\Rohit\\Desktop\\myhapp1.apk")
    execute_adb("adb install -r myhapp1.apk")
    execute_adb("adb shell input keyevent 26")
    execute_adb("adb shell  input swipe 10 1000 10 10")
         #execute_adb("adb shell am instrument -w -m    -e package com.example.mhyapp -e debug false            #com.example.mhyapp.test/androidx.test.runner.AndroidJUnitRunner")
  else :
    print("device not detected")
    sys.exit()

def setup() :
  print("")
  print("                    *         **       *   *       **              **     *   *    *****    ****    *   *    **      *****    *    ****    *     *")
  print("                    *        *  *      *   *      *  *            *  *    *   *      *      *  *    * * *   *  *       *      *    *  *    * *   *")
  print("                    *        ****      *   *      ****            ****    *   *      *      *  *    *   *   ****       *      *    *  *    *   * *")
  print("                    ****     *  *        *        *  *            *  *    *****      *      ****    *   *   *  *       *      *    ****    *     *"    )
  
  #print(" **     *   *    *****    ****    *   *    **      *****    *    ****    *     *" )
  #print("*  *    *   *      *      *  *    * * *   *  *       *      *    *  *    * *   *"   )
  #print("****    *   *      *      *  *    *   *   ****       *      *    *  *    *   * *")
  #print("*  *    *****      *      ****    *   *   *  *       *      *    ****    *     *")
  print("\n\n")
  print("\t\t\t\t\t\t****   ****      **      * *     ****     *   *    ****    ****    *   *")
  print("\t\t\t\t\t\t*      *  *     *  *    * * *    *        *   *    *  *    *  *    *  *  ")
  print("\t\t\t\t\t\t****   **       ****    *   *    ****     *   *    *  *    **      * * ")
  print("\t\t\t\t\t\t*      * *      *  *    *   *    *        * * *    *  *    * *     *  *")
  print("\t\t\t\t\t\t*      *   *    *  *    *   *    ****     *   *    ****    *   *   *    *")
  print("\n\n\n\n")
  
  print("\t\t\t\t\t\t\t\tSelect from the following : \n")
  print("\t\t\t\t\t\t\t     ******************************** \n")
  print("\t\t\t\t\t\t\t\t1. Warm Launch Latency \n")
  print("\t\t\t\t\t\t\t\t2. Cold Launch Latency\n")
  print("\t\t\t\t\t\t\t\t3. Janky frames\n")
  print("\t\t\t\t\t\t\t\t4. Monkey test\n")
  option = input("\t\t\t\t\t\t\t\t"); 
  print("NOTE : The realted test results ( log file , excel) will be stored in the local install directory")
  if option == "1":
      print(" Input iteration count of each app...")
      option1=input()
      setCountEachApp(option1)
      setFileName("warmlaunch.csv")
      warmLaunch()     
  elif option == "2":
      print(" Input iteration count of each app...",end=' ')
      option1=input()
      setCountEachApp(option1)
      setFileName("coldlaunch.csv")
      coldLaunch()
  elif option =="3":
      print(" Input iteration count of each app...")
      option1=input()
      setCountEachApp(option1)
      print("Janky frames")
      #startJankyFramesTest()
      startJankyFrameTest()

  elif option =="4":
     print("Running monkey test")
     setFileName("monkeytest.txt")
     startMonkeyTest()
  else :
     print("wrong option selected")
     
     
setup()

#execute_adb("adb devices")