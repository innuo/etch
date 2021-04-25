import sys
import time
import RPi.GPIO as GPIO

# define variables
chan_list_l = [17,27,22,23] # GPIO ports to use
chan_list_r = [19,26,16,20] # GPIO ports to use

delay=.001 # delay between each sequence step

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Set all pins as output
for pin in chan_list_l + chan_list_r:
  print ("Setup pins")
  GPIO.setup(pin,GPIO.OUT)

def setStepper(chan_list, bits):
    GPIO.output(chan_list, bits)
    time.sleep(delay)

arr = [[1, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1],[0, 1, 1, 0],[0, 0, 1, 0],[1, 1, 0, 0],[0, 1, 0, 0]]

def forwardStep(steps=100, left=True):
    if left:
        chan_list = chan_list_l
    else:
        chan_list = chan_list_r
            
    for i in range(steps):
        for x in arr:        
            setStepper(chan_list, x)

def backwardStep(steps=100, left=True):
    if left:
        chan_list = chan_list_l
    else:
        chan_list = chan_list_r
    for i in range(steps):
        for x in reversed(arr):        
            setStepper(chan_list, x)
            
def userInput():
    while True:
      try:
        print("......")
        print("How much left motor?")
        l = int(input())
        print("How much right motor?")
        r = int(input())

        if l > 0:
            forwardStep(abs(l), True)
        else:
            backwardStep(abs(l), True)
        if r > 0:
            forwardStep(abs(r), False)
        else:
            backwardStep(abs(r), False)
            
      except KeyboardInterrupt:
        GPIO.output(chan_list_l, (0,0,0,0))
        GPIO.output(chan_list_r, (0,0,0,0))
        sys.exit()

def userInputOl():
    while True:
      try:
        print("......")
        print("which motor ?")
        if input().lower() == 'l':
            left = True
        else:
            left = False
            
        print("forward ? ")
        f = input()
        print("steps: ")
        s = int(input())
        if s > 100:
            s = 100
        if s < 0:
            s = 0
        if f.lower()[0] == "y":
            forwardStep(s, left)
        else:
            backwardStep(s, left)
       
      except KeyboardInterrupt:
        GPIO.output(chan_list_l, (0,0,0,0))
        GPIO.output(chan_list_r, (0,0,0,0))
        sys.exit()
    
if __name__ == '__main__':
   
    #forwardStep(546)
    #backwardStep(546) #approx 2 pi

    userInput()
    GPIO.output(chan_list_l, (0,0,0,0))
    GPIO.output(chan_list_r, (0,0,0,0))
    sys.exit()
    

    
