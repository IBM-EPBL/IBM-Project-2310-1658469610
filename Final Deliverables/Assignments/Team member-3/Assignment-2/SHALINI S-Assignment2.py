
#ASSIGNMENT-2

"""Build a python code,Assume u get Temperature and Humidity values (generated with random function to a variable ) and write a condition to continuously detect alarm in case of high temperature """

import random
import time

while(1):
    
  temperature=random.randint(0,200)  #TO GENERATE RANDOM NUMBER FOR TEMPERATURE
  
  print("Temperature="+str(temperature)+"°F")
  print("Temperature in celcius : "+str(((temperature-32)*5)//9)+"°C")
  
  if(temperature>50):        #IF TEMPERATURE GOES HIGH THEN ALARM IS ON
      print("Temperature is too high")
      print("The Alarm is ON")
      
  else:       #TEMPERATURE VALUE GOES NORMAL THEN ALARM IS OFF 
      print("Temperature is normal")
      print("The Alarm is OFF")
      
  
  
  humidity=random.randint(0,100)  #TO GENERATE RANDOM NUMBER FOR HUMIDITY
  print("Humidity="+str(humidity)+"%")

  if(humidity<50):
      print("Humdity is less than 50")

  else:
       print("humidity is greater than 50")


  time.sleep(2)

  
