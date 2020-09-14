from win10toast import ToastNotifier
import datetime
import pyttsx3

#Function to send notification on your desktop
def notification(sub):
    n = ToastNotifier()
    n.show_toast(sub,duration = 15)  

#Function to convert text to speech using pyttsx3 module
def voice():
    engine = pyttsx3.init() 
    engine.say('Hello Parag, it is time for you to attend your class.') 
    engine.runAndWait()

#function to read text file in "day,time,subject" format
def read_file():
    l = []
    textfile = open('TimeTable.txt','r')
    lines = textfile.readlines()      #Reads line by line
    for i in range(0,len(lines)):
        li = lines[i].split(',')
        l.append(li)
    textfile.close()
    return l
    
def alarm(how_early,set_day,set_time,subject):
    while True:        #Since funtion has to be running continuously, use loop
        x = datetime.datetime.now()
        x = x.strftime("%A")          #Displays current day
        
        current_time = datetime.datetime.now()      #Displays current time
        change_time = datetime.timedelta(minutes = how_early)
        new_time = current_time + change_time
        new_time = str(new_time)                    #Convert to string to compare
        datee,timee = new_time.split(' ')           
        timee = timee.split('.')                    #Split at "." to eliminate values after decimal point
        
        if set_day != x:                          
            break
        
        if timee[0] == set_time and set_day == x:
            voice()                             #call voice function to remind you of your task
            notification(subject)               #call notification function to display notification
            break                               #break out of loop once task has been completed
        
        check = set_time
        pass_time = datetime.datetime.strptime(check,'%H:%M:%S')
        passed_time = pass_time.time()
        
        if current_time.time() > passed_time:   #To check if current time has already passed time passed to the alarm function
            break

#Main Application
r = read_file()
for i in range(0,len(r)):
    d = r[i][0]
    t = r[i][1]
    s = r[i][2]
    alarm(10,d,t,s)     
