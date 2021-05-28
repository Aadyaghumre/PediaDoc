import speech_recognition as speech
import pyttsx3
import pygame
import PediaDocDictionary as dictionary



pygame.init()

width = 900
height = 600
screen=pygame.display.set_mode((width, height))

pygame.display.set_caption('PEDIADOC')

image = pygame.image.load("Images/welcome.jpg").convert_alpha() 
image1=pygame.transform.scale(image, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()

a = pyttsx3.init()
a.setProperty('Rate',100)
a.say("Hello  I am your pediadoc assistant. You can ask for vaccines above and below 18 and medicines for children of age 18 and below..  Press d to interact")
a.runAndWait()

bg1=pygame.image.load("images/bg1.jpg").convert_alpha()
image=pygame.transform.scale(bg1, (800,650))
screen.blit(image,(0,0))
pygame.display.update()        
    
            

keypress = "none"
exitstatus = "no"

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keypress = 'd'
                    
        if keypress =="d":
            bg2 = pygame.image.load("images/bg2.jpg").convert_alpha()
            image=pygame.transform.scale(bg2, (900,600))
            screen.blit(image,(0,0))
            pygame.display.update()
                    
            r=speech.Recognizer()            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
           
            matchfound = 0    
            for kw in dictionary.dictn:
                if matchfound == 1:
                    break
                if kw in command:
                    matchfound = 1
                    if dictionary.dictn[kw][0] == "Spch":
                        a.say(dictionary.dictn[kw][1])
                        a.runAndWait()
                        print(dictionary.dictn[kw][1])
                        
                    if dictionary.dictn[kw][0] == "ImgSpch":                
                        image = pygame.image.load("Images/"+dictionary.dictn[kw][2]).convert_alpha() 
                        image1=pygame.transform.scale(image, (570,500))
                        screen.blit(image1,(150,100))
                        pygame.display.update()
                        
                        print(dictionary.dictn[kw][1])
                        
                        a.say(dictionary.dictn[kw][1])
                        a.runAndWait()
                        
                    
                    if dictionary.dictn[kw][0] == "close":
                        image = pygame.image.load("Images/close.png").convert_alpha() 
                        image1=pygame.transform.scale(image,(500,400))
                        screen.blit(image1,(150,100))
                        pygame.display.update()
                        
                        a.say(dictionary.dictn[kw][1])
                        a.runAndWait()                        
                        exitstatus ="yes"
                        break
           
        if exitstatus =="yes":
            pygame.quit()
            break
                       
        keypress ="none" 
        bg1=pygame.image.load("images/bg1.jpg").convert_alpha()
        image=pygame.transform.scale(bg1, (900,600))
        screen.blit(image,(0,0))
        pygame.display.update()               
            
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break       
            
            
            
            
            
            
            
                    
                    