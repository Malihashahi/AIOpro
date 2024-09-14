#import libary
import pyautogui  as robot

#use sleep funtion
robot.sleep(3)
#use for  to print text in time loop  with take it rage
for x in range(1,10):
    robot.sleep(0.3)
    robot.write('i love you...', interval=0.05)
    robot.press('enter')