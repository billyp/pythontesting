print ("hello world")
print ("chuck, this is billy, HI!")
print ("this after my 2nd commit")

import sys

ans=True
while ans:
    print ("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      print("\n Student Added") 
    elif ans=="2":
      print("\n Student Deleted") 
    elif ans=="3":
      print("\n Student Record Found") 
    elif ans=="4":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 

