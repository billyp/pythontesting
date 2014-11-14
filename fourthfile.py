print ("hello world")
print ("this program multiplies")
import sys

ans=True
while ans:
    print ("""
    1.Multiply variable by 1
    2.Multiply variable by 2
    3.Exit/Quit
    """)
    '''Begin multiline comment
    Body of multiline comment
    notes to self
    == asigns a variable
    = evaluates the variable
    End of multiline comment'''
    print ("The number to be mulitplied is TWO")
    multiplier=100
    ans=input("What would you like to do? ") 
    print (multiplier)
    if ans=="1":
      shortval=multiplier*1
      print("\n Multiplied by 1 =")
      print(shortval)
    elif ans=="2":
      print("\n Multiplied by 2") 
    elif ans=="3":
      print("\n Goodbye") 
      ans=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 

