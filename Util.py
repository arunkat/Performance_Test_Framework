## Arun K. singh Rohit Nehra

import subprocess
from subprocess import Popen, PIPE, check_output, CalledProcessError
import time
import os
import signal
import functools
import re
from MyFile import *
import csv
from collections import defaultdict
import re
import msvcrt as m
def wait():
    m.getch()

from tempfile import TemporaryFile
def __getout(*args):
    with TemporaryFile() as t:
        try:
            out = check_output(args, stderr=t)
            return  0, out
        except CalledProcessError as e:
            t.seek(0)
            return e.returncode, t.read()

# cmd is string, split with blank
def getout(cmd):
    cmd = str(cmd)
    args = cmd.split(' ')
    return __getout(*args)

def bytes2str(bytes):
    return str(bytes, encoding='utf-8')

def isAdbConnected():
    cmd = 'adb devices'
    (code, out) = getout(cmd)
    if code != 0:
        print('something is error')
        return False
    outstr = bytes2str(out)
    print(outstr)
    #TODO if there is any better way to identify if device is connected
    #if " device" in outstr:
    if re.search(r'\bdevice\b',outstr):
        print("device is connected");
        return True
    else:
        print("no devices")
        return False

def addToExcel(filename):
  #filename = "warmLaunch.csv"
  header = ("Serial number","App","itearion 1 " ,"iteration 2","iteration 3","iteration 4 ","iteration5 ")
  data = [
  (1,"whatsapp",1,2,3,4,5),
  (5,"settings",6,7,8,9,10)
  ]
def writer(data):
  filename = getFileName()
  header = ("App","itearion 1 " ,"iteration 2","iteration 3","iteration 4 ","iteration5 ")
  #data = [
  #(1,"whatsapp",1,2,3,4,5)
  #(5,"settings",6,7,8,9,10)
  #]
  with open (filename, "w", newline = "") as csvfile:
    fieldnames = ['settings'] 
    #writer = csv.DictWriter(csvfilefieldnames=fieldnames)
    writer = csv.writer(csvfile)
    #for values in zip(*header):
    writer.writerow(data)
    for values in zip(*data.values()):
            writer.writerow(values)
    #for x in data:
     # writer.writerow(x)
    #for key, value in data.items():
     #  writer.writerow([key, value])
    #for key , value in data.items():
     #   row = list(key)
      #  row = [row[0]] + row[1]
        
       # writer.writerow(row)
        #row += list(company) if company is not None else ['', '']  # Write empty fields if no company
       #writer.writerow('{0},{1}\n'.format(key, value))
#isAdbConnected()

#converts s/ms string to integer decimal format time 
def format_time_int(tim):
  tim = tim.rstrip("ms")
  #tim = tim.rstrip("s")
  tim = tim.replace("s",".")
  
  
  return(tim)

def readLogsInSeperateThread():
# this is just called once , just store the time and the app name and send it after it recieves a signal from the main thread
  """subprocess.Popen(['adb', 'shell', 'dumpsys','meminfo'], stdout=subprocess.PIPE, text=True) #universal_newlines=True)
  proc1 = subprocess.Popen(['adb', 'shell', 'dumpsys', 'meminfo'], stdout=subprocess.PIPE, universal_newlines=True, errors='ignore')
  
  for lin in proc1.stdout:
    if "Free RAM:" in lin:
       print(lin)
  """
  launchDict = defaultdict(list)
  appList = []
  lCount = 1
  #time.sleep(1)
  subprocess.Popen(['adb', 'logcat', '-c'], stdout=subprocess.PIPE, text=True) #universal_newlines=True)
  proc = subprocess.Popen(['adb', 'logcat', '-v', 'time'], stdout=subprocess.PIPE, universal_newlines=True, errors='ignore')
  matches =["facebook","instagram","whatsapp","amazon","youtube","gaana","paytm","olacabs","truecaller","contacts"]  
  appname1=" "
  ap=" "
  #import ART 
  for line in proc.stdout:
       if " Displayed " in line:
          #proc.kill()
          #print(line)
          appName = re.search(r' Displayed (.*?)\/', line).group(1)
          ap0=getlastActivityLoaded()
          ap=line.split("/")[-1].split(":")[0]
          #print("found activity",ap,"launched activity",ap0) 
          appname1=getlastPackageLoaded()
          #print(appname1,ap0)
          
          appname= appName.split(".")
          if ((appname1 == appName) and (ap0!=ap) and (appname1 !="com.whatsapp") and (appname1!="in.amazon.mShop.android.shopping") \
              and (appname1!="com.olacabs.customer") and (appname1!="net.one97.paytm") and (appname1!="com.truecaller")              \
              and (appname1!="com.instagram.android") and (appname1!="com.facebook.katana") ): 
                #print("found different activity kipping ..[",ap,ap0,"]",appName);
                continue;
          elif (appname1 !=appName):
                #print("mismatching package name found , skipping")
                continue; 
          else:
                ap0=ap
                     
          #print("2",appname,appname1);
          #appname1=appname;
          lCount = lCount + 1
          #if (lCount > launchCount):

          timeToLaunch = line.split("+",1)[1]
          timeToLaunch = timeToLaunch.rstrip("\n")
          timeToLaunch_ms = timeToLaunch.rstrip("ms")
          timeToLaunch_s = timeToLaunch.replace("s",".")
          #print(timeToLaunch_s,timeToLaunch_ms)
          ttl=format_time_int(timeToLaunch);
          
          l=list(set(matches) & set(appname))
          #l=[x in appname if x in matches]
          if (len(ttl) <4 ):
            print(l,"Launch Time = [","0.",ttl,"s]")
          else:
            print(l,"Launch Time = [",ttl,"s]")
          #print(timeToLaunch)
          appList.append((appName,timeToLaunch))
          #setBack(True)
          #launchDict.update( {appName : timeToLaunch} )          
          #writer([(appName,timeToLaunch)])
                
       if not getShouldLogRun():
         #print(launchDict)
         #print("Stopping now ...")
         #print(appList)
         for key,value in appList:
           launchDict[key].append(value)
         print(launchDict) 
         writer(launchDict)
         #for key,value in launchDict.items():
          # print(key ,value)
         break

  
         proc.kill()
         #proc1.kill()
         print(launchDict)
  #input("Press Enter to Quit.....");
  #proc.wait()
  #with Popen('adb logcat', stdout=PIPE, universal_newlines=True) as process:  
   # for byteline in iter(p.stdout.readline, ''):
   #    line = byte_line.decode('utf8', errors='backslashreplace').replace('\r', '')
    #   process_stdout(line)
   #   if " Displayed " in line:
    #     print(" Disaplyed "+line)
    #     print (line.split("+",1)[1])
                
    #   if not getShouldLogRun():
    #     print("shouldRun is false")
    #     break
     #    proc.kill()
         #proc.wait()
