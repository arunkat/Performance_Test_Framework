global allApps
#allApps = ['com.google.android.contacts/com.android.contacts.activities.PeopleActivity']
#allApps= ['com.instagram.android/com.instagram.mainactivity.MainActivity']
#allApps = ['com.android.settings/.Settings','com.android.dialer/.app.DialtactsActivity']
#allApps =['com.instagram.android/com.instagram.mainactivity.MainActivity']
#sallApps =['com.google.android.dialer/com.android.dialer.main.impl.MainActivity','com.google.android.apps.messaging/.home.HomeActivity']
#allApps = ['com.instagram.android/com.instagram.mainactivity.MainActivity','com.android.settings/.Settings','com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity','com.facebook.katana/.LoginActivity','com.google.android.apps.maps/com.google.android.maps.MapsActivity','com.google.android.apps.messaging/.ui.ConversationListActivity','com.google.android.contacts/com.android.contacts.activities.PeopleActivity']
#allApps1 = [ 'com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity','com.facebook.katana/.LoginActivity' ]
#allApps = ['com.whatsapp/.HomeActivity','com.gaana/.SplashScreenActivity','in.amazon.mShop.android.shopping/com.amazon.mShop.navigation.MainActivity','net.one97.paytm/.app.LauncherActivity','com.olacabs.customer/.ui.SplashActivity','com.truecaller/.ui.TruecallerInit','com.instagram.android/.MainActivity','com.facebook.katana/.LoginActivity','com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity']
allApps = ['in.amazon.mShop.android.shopping/com.amazon.mShop.home.HomeActivity','net.one97.paytm/.app.LauncherActivity','com.olacabs.customer/.ui.SplashActivity','com.truecaller/.ui.TruecallerInit','com.instagram.android/com.instagram.mainactivity.MainActivity','com.facebook.katana/.LoginActivity','com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity']
#allApps=['com.facebook.katana/.LoginActivity']
#allApps=['com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity']

def setMultiRuninLoop(z):
    global multiRun
    multiRun=z
    print(multiRun) 

def getMultiRuninLoop():
    return multiRun

def setCountEachApp(z):
    global CountEachApp
    CountEachApp=z
    #print(CountEachApp) 

def getCountEachApp():
    return CountEachApp

def setlastPackageLoaded(z,z1):
    global lastPackage
    global lastActivity
    lastPackage=z1
    lastActivity=z
    #print(lastPackage,lastActivity) 

def getlastPackageLoaded():
    return lastPackage

def getlastActivityLoaded():
    return lastActivity

def setShouldLogRun(z):
   global shouldLog
   shouldLog = z
   print(shouldLog)
   
def getShouldLogRun():
    return shouldLog
    
def setFileName(filename):
    global file
    file = filename

def getFileName():

    return file     
    
def setBack(arg):
    global back
    back = arg
    
def getBack():
    return back    