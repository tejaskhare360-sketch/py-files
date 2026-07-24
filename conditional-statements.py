#simple traffic light program 

light = input("enter the colour of the traffic light (red, yello, green): ")

if light == "red":
    print("stop!")

elif light == "yellow":
    print("get ready!")

elif light == "green": 
    print("go!")

else: 
    print("invalid input!")


#-----------------------------------------------#

#loop version of the above program

while True:
    light = input("enter the colour of the traffic light (red, yellow, green): ")
    if light == "break":
        break
    if light == "red":
        print("stop!")

    elif light == "yellow":
        print("get ready!")

    elif light == "green":
        print("go!")
    else:
        print("invalid input!")

#type 'break' to exit the loop

