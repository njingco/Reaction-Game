import RPi.GPIO as GPIO
import time


from time import sleep
from random import uniform


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#--------------------------------------------------------LED (Timer)----------------------------------------------------------------------------

#Green
GPIO.setup(16, GPIO.OUT)

#Blue
GPIO.setup(20, GPIO.OUT)

#Red
GPIO.setup(21, GPIO.OUT)


#--------------------------------------------------------7 Segment---------------------------------------------------------------------

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


points1= -1
points2 = 0
rounds = -1
start =1


#--------------------------------------------------------Button-----------------------------------------------------------------------------

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    
    input_state2 = GPIO.input(24)
    if  input_state2==False:
        points2 = points2 + 1
        rounds = rounds +1
        print ("2:", points2)
        time.sleep(0.2)
    
    input_state1 = GPIO.input(18)
    if  input_state1==False :
        points1 = points1 + 1
        rounds = rounds + 1
        print ("1:",points1)
        time.sleep(0.2)

    if input_state1==False or input_state2==False:
    



##---------------------------------------------------------Game Start------------------------------------------------------------------
    
        
#######################PLAYER 1#######################
#--------------------0 (A, B, C, D, E, F)--------------------------    
        if rounds ==0:
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, True)

            #G
            GPIO.output(10, False)

            #E
            GPIO.output(9, True)

            #D
            GPIO.output(11, True)

            start=0


#--------------------1-(B, C)-------------------------
            
        elif rounds ==1:
            
            time.sleep(0.1)
            #A
            GPIO.output(2, False)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, False)

            #G
            GPIO.output(10, False)

            #E
            GPIO.output(9, False)

            #D
            GPIO.output(11, False)

            start =0

#--------------------2 (A, B, G, E, D)-------------------------
            
        elif rounds == 2 : 

            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, False)

            #F
            GPIO.output(22, False)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, True)

            #D
            GPIO.output(11, True)


            start =0
            
#--------------------3 (A, B, G, C, D, )-------------------------
            
        elif rounds  ==3:
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, False)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, False)

            #D
            GPIO.output(11, True)

            start =0
                

#--------------------4 (F, G, B, C)-------------------------
            
        elif rounds  ==4 :
            time.sleep(0.1)
            #A
            GPIO.output(2, False)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, True)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, False)

            #D
            GPIO.output(11, False)

            start =0
            
#--------------------5 (A, F, G, C, D )-------------------------

        elif rounds  == 5:
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, False)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, True)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, False)

            #D
            GPIO.output(11, True)

            
            if points1 ==5 or points2 ==5:
                start = 1

            else:
                start =0
                
#--------------------6 (A, F, G, E, D, C)-------------------------
            
        elif  rounds  ==6 :
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, False)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, True)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, True)

            #D
            GPIO.output(11, True)

            if points1 == 5 or points2 ==5:
                start += 1

            else:
                start =0       

#--------------------7 (A, B, C )-------------------------
            
        elif  rounds  ==7:
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, False)

            #G
            GPIO.output(10, False)

            #E
            GPIO.output(9, False)

            #D
            GPIO.output(11, False)

            if points1 ==5 or points2 ==5:
                start += 1

            else:
                start =0    

#--------------------8 (ALL)-------------------------
            
        elif  rounds  ==8 :
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)
            
            #F
            GPIO.output(22, True)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, True)

            #D
            GPIO.output(11, True)

            if points1 ==5 or points2 ==5:
                start += 1

            else:
                start =0
                
#--------------------9 (A, B, F, G, C, D )-------------------------
            
        elif rounds  ==9 :
            time.sleep(0.1)
            #A
            GPIO.output(2, True)

            #B
            GPIO.output(3, True)

            #C
            GPIO.output(4, True)

            #F
            GPIO.output(22, True)

            #G
            GPIO.output(10, True)

            #E
            GPIO.output(9, False)

            #D
            GPIO.output(11, True)
            

#----------------------------END LED--------------------------------

            
        if points1 >= 5 and points2 < 5:

            #OFF
            time.sleep(0.1)
            GPIO.output(2, False)
            GPIO.output(3, False)
            GPIO.output(4, False)
            GPIO.output(22, False)
            GPIO.output(10, False)
            GPIO.output(9, False)
            GPIO.output(11, False)
            time.sleep(0.1)
            
            for i in range (5):
                GPIO.output(20, False)
                sleep(.5)

                GPIO.output(20, True)
                sleep(.5)
                GPIO.output(20, False)

                points1 = -1
                points2 = 0
                rounds =-1
                
        if points2 >=5 and points1 < 5:

            #OFF
            time.sleep(0.1)
            GPIO.output(2, False)
            GPIO.output(3, False)
            GPIO.output(4, False)
            GPIO.output(22, False)
            GPIO.output(10, False)
            GPIO.output(9, False)
            GPIO.output(11, False)
            time.sleep(0.1)
            
            for i in range (5):
                GPIO.output(21, False)
                sleep(.5)

                GPIO.output(21, True)
                sleep(.5)
                GPIO.output(21, False)
                
            points1 = -1
            points2 = 0
            rounds =-1


            

#------------------------------------------------------------START LED------------------------------------------------------

        if points1 >=0 or points2 >=0:  
           
                
            if points1 ==5 and points2 <5:
                sleep(.2)
                GPIO.output(16, False)
                
                
            elif points2 ==5 and points2 <5:
                sleep(.2)
                GPIO.output(16, False)
                
            elif points1 <=5 and points2 <=5:
               if start == 0 :
                    GPIO.output(16, False)
                    sleep(uniform(.1, 5))

                    GPIO.output(16, True)
                    sleep(.2)
                    GPIO.output(16, False)

                    start +=1

            

        

                    
                


GPIO.cleanup()

