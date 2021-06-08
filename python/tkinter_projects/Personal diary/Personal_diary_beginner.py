import os 
import datetime

print("Welcome to Personal_dairy.")
now = datetime.date.today()
print("Current date and time: "+(str(now))+"\n")

page = open(str(now)+".txt", "w")
lines = input("Todays entry:- ")
page.write(lines+"\n")
page.close()
