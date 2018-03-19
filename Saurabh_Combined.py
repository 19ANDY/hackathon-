import serial
import time
import smtplib
import os,sys as sis
import winsound
import MySQLdb
 
ArduinoSerial1 = serial.Serial('com17',9600)
ArduinoSerial2 = serial.Serial('com13',9600)
time.sleep(2)
t = 9897550614153
r = 26390579686429
s = 73669285398244
u = 73669285449134
print ("Enter your choice")
print ("1. For RFID card detection")
print ("2. For dual security using face and voice recognition")
x = input()
while true:
        if(x==1):
                print ""
                print ("Please present your RFID card")
                y= int(ArduinoSerial1.readline(),16)
           
                if y == t:
                        print "RFID found : Welcome Rishabh, Your ID is",y
                        ArduinoSerial2.write('1')
                        print "Gate Unlocked"
                        time.sleep(1)
                        ArduinoSerial2.write('0')
                        db = MySQLdb.connect(host="localhost",user="aecs1",passwd="aecs1",db="home")
                        cur = db.cursor()
                        cur.execute("INSERT INTO access(RFID,NAME,EMAIL) VALUES('9897550614153','Rishabh','geniusrishabhanand@gmail.com')")
                        db.commit()
                        db.close()
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login("radheysen0@gmail.com","9413261316")
                        server.sendmail("radheysen0@gmail.com","geniusrishabhanand@gmail.com","Hi Admin, Rishabh has entered your house")
                        server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Rishabh has entered your house")
                        server.quit()
                
                elif y == r:
                        print "RFID found :Welcome Saurabh, Your ID is",y
                        ArduinoSerial2.write('1')
                        print "Gate Unlocked"
                        time.sleep(1)
                        ArduinoSerial2.write('0')
                        db = MySQLdb.connect(host="localhost",user="aecs1",passwd="aecs1",db="home")
                        cur = db.cursor()
                        cur.execute("INSERT INTO access(RFID,NAME,EMAIL) VALUES('26390579686429','Saurabh','saurabh2206@gmail.com')")
                        db.commit()
                        db.close()
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login("radheysen0@gmail.com","9413261316")
                        server.sendmail("radheysen0@gmail.com","geniusrishabhanand@gmail.com","Hi Admin, Saurabh has entered your house")
                        server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Saurabh has entered your house")
                        server.quit()
                elif y == s:
                        #print "found"
                        print "RFID found :Welcome Sangamitra, Your ID is",y
                        ArduinoSerial2.write('1')
                        print "Gate Unlocked"
                        time.sleep(1)
                        db = MySQLdb.connect(host="localhost",user="aecs1",passwd="aecs1",db="home")
                        cur = db.cursor()
                        cur.execute("INSERT INTO access(RFID,NAME,EMAIL) VALUES('73669285398244','Sangamitra','johrisangamita@gmail.com')")
                        db.commit()
                        db.close()
                        ArduinoSerial2.write('0')
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login("radheysen0@gmail.com","9413261316")
                        server.sendmail("radheysen0@gmail.com","geniusrishabhanand@gmail.com","Hi Admin, Sangamitra has entered your house")
                        server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin, Sangamitra has entered your house")
                        server.quit()
                elif y == u:
                        print "Sorry,Gate locked"
                        winsound.Beep(1000,2000)
                        time.sleep(1)
                        ArduinoSerial2.write('0')
                        db = MySQLdb.connect(host="localhost",user="aecs1",passwd="aecs1",db="home")
                        cur = db.cursor()
                        cur.execute("INSERT INTO access(RFID,NAME,EMAIL) VALUES('73669285449134','Unknown','Unknown')")
                        db.commit()
                        db.close()
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login("radheysen0@gmail.com","9413261316")
                        server.sendmail("radheysen0@gmail.com","geniusrishabhanand@gmail.com","Hi Admin,"+str(u)+ " has tried to enter your house")
                        server.sendmail("radheysen0@gmail.com","saurabh2206@gmail.com","Hi Admin,"+str(u)+ " has tried to enter your house")
                        server.quit()
                
                else:
                        print "RFID Not found "
                        db = MySQLdb.connect(host="localhost",user="aecs1",passwd="aecs1",db="home")
                        cur = db.cursor()
                        db.close()
                        winsound.Beep(1000,2000)
        #if(x==2):
		
