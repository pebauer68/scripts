#!/usr/bin/env python3.8
#connect with python to a Gambas GUI server
import socket,threading,time,os
from datetime import datetime
GUI_SERVER="localhost"    #gloabal vars
GUI_PORT=9090
send_time=True

class GuiClient:
  def conn(self):
    global client   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((GUI_SERVER,GUI_PORT))  
  def send(self,object):
    client.sendall((object +"\n").encode())  #to utf8  
  

  def getline(self):
    alldata = b"" 
    while (newdata := client.recv(1024)) != b'':  
      alldata += newdata
      #print (alldata)
      if b"\n" in alldata:
        return alldata.decode('utf-8').rstrip()  
    print ("Disconnected, no data !!!")
    client.close()
    threading._shutdown()
    
    
  def receive(self): 
    global send_time   
    while True:
      event = self.getline()
      print ("EV: " + event)
      if event == "Button1_clicked":
         send_time=False
      if event == "Button2_clicked":
         send_time=True
      if event == "Button3_clicked":
         self.send("textarea1.text, ")
      if event == "Button4_clicked":
         self.send("Textarea1.text")
         response = self.getline()
         self.send("Textarea1.text," + response.upper())
      if event == "Button5_clicked":
         self.send("Textarea1.text")
         response = self.getline()
         self.send("Textarea1.text," + response.lower()) 
      if event == "FMain_closed":
         exit

mygui = GuiClient()
mygui.conn()
threading.Thread(target=mygui.receive,daemon=True).start()

mygui.send ("textlabel1.text,python + gambas = pytbas")
mygui.send ("button1.text,stop")
mygui.send ("button2.text,continue")
mygui.send ("button3.text,clear texrarea")
mygui.send ("button4.text,do Text.upcase")
mygui.send ("button5.text,do Text.downcase")
mygui.send ("FMain.Text,Pytbas")               #set title of Application
mygui.send ("Textarea1.Text,hello-textarea")

while True:
    if send_time: 
          mygui.send("Textbox1.Text" + "," + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
          time.sleep(1)  

