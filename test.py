import sys
import time
import RPi.GPIO as GPIO
import pygame

# define variables
chan_list_l = [17,27,22,23] # GPIO ports to use
chan_list_r = [19,26,16,20] # GPIO ports to use

init_delay=.001 # delay between each sequence step

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Set all pins as output
for pin in chan_list_l + chan_list_r:
  print ("Setup pins")
  GPIO.setup(pin,GPIO.OUT)

def close_motors():
    GPIO.output(chan_list_l, (0,0,0,0))
    GPIO.output(chan_list_r, (0,0,0,0))

def setStepper(chan_list, bits, delay=init_delay):
    GPIO.output(chan_list, bits)
    time.sleep(delay)

arr = [[1, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1],[0, 0, 0, 1],[0, 1, 1, 0],[0, 0, 1, 0],[1, 1, 0, 0],[0, 1, 0, 0]]

def forwardStep(steps=100, left=True):
    if left:
        chan_list = chan_list_l
    else:
        chan_list = chan_list_r

    for i in range(steps):
        delay = init_delay
        if steps > 20:
          delay =  init_delay * 1.5
          
        for x in arr:        
            setStepper(chan_list, x, delay)

def backwardStep(steps=100, left=True):
    if left:
        chan_list = chan_list_l
    else:
        chan_list = chan_list_r

    for i in range(steps):
        delay = init_delay
        if steps > 20:
          delay =  init_delay * 1.1
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


def keyboard_control(steps=10):
  pygame.init()
  screen = pygame.display.set_mode([60,60])
  clock = pygame.time.Clock()
  pygame.key.set_repeat(100,100)
  while True:
    for event in pygame.event.get():
      keys = pygame.key.get_pressed()
      
      if event.type == pygame.QUIT:
        close_motors()
        pygame.quit()
        return
              
      if event.type == pygame.KEYDOWN:
        if keys[pygame.K_RIGHT] + keys[pygame.K_UP] + keys[pygame.K_LEFT] + keys[pygame.K_DOWN] > 1:
          x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
          y = keys[pygame.K_UP] - keys[pygame.K_DOWN]
          print('x',x)
          print('y',y)
          x,y = int(x*steps/(2**.5)), int(y*steps/(2**.5))

          for z in range(steps):
            a=1
                
        else:
          if event.key == pygame.K_UP:
            #rightMotor.rotate(step)
            print("Up was pressed.")
            #counter['up'] += step

          elif event.key == pygame.K_DOWN:
            #rightMotor.rotate(-step)
            print("Down was pressed.")
            #counter['down'] += step

          elif event.key == pygame.K_LEFT:
            #leftMotor.rotate(-step)
            print("Left was pressed.")
            #counter['left'] += step
                      
          elif event.key == pygame.K_RIGHT:
            #leftMotor.rotate(step)
            print("Right was pressed.")
            #counter['right'] += step
                        
          elif event.key == pygame.K_ESCAPE:
            close_motors()
            pygame.quit()
            return
            
  

def userInputl():
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

    #userInput()
    keyboard_control()
  
    GPIO.output(chan_list_l, (0,0,0,0))
    GPIO.output(chan_list_r, (0,0,0,0))
    sys.exit()
    

    
