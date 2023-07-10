import pygame
import os
pygame.font.init()
pygame.mixer.init()


width, height=1500,800
bgcolor=(154,113,60)
FPS=60
speed=5

weapon_vel=20
max_weapon=6

hit=pygame.USEREVENT+1

weapon_color=(235,184,20)

health_font=pygame.font.SysFont('comicsans',20)

wining_font=pygame.font.SysFont('comicsans',100)

timer_font=pygame.font.SysFont('comicsans',20)




win=pygame.display.set_mode((width, height))
img=pygame.image.load('icon.jpeg')
pygame.display.set_icon(img)
pygame.display.set_caption("Gluttonous")
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow,(80,100))
arrow=pygame.transform.rotate(arrow,270)
arrowtilted=pygame.image.load('arrowtilted.png')
arrowtilted=pygame.transform.rotate(pygame.transform.scale(arrowtilted,(50,30)),45)





bgimage=pygame.image.load(os.path.join('bcki.png'))

size=pygame.transform.scale(bgimage,(width,height))

character1=pygame.image.load(os.path.join('character.gif'))
size_c=pygame.transform.scale(character1,(150,160))


apple=pygame.image.load(os.path.join('apple.png'))
size_a=pygame.transform.rotate(pygame.transform.scale(apple,(35,35)),330)


banana=pygame.image.load(os.path.join('banana.png'))
size_b=pygame.transform.rotate(pygame.transform.scale(banana,(50,50)),330)


watermelon=pygame.image.load(os.path.join('watermelon.png'))
size_w=pygame.transform.rotate(pygame.transform.scale(watermelon,(50,50)),330)


grapes=pygame.image.load(os.path.join('grape.png'))
size_g=pygame.transform.rotate(pygame.transform.scale(grapes,(50,50)),330)


pineapple=pygame.image.load(os.path.join('pineapple.png'))
size_p=pygame.transform.rotate(pygame.transform.scale(pineapple,(60,60)),330)


stone=pygame.image.load(os.path.join('stone.png'))
size_s=pygame.transform.rotate(pygame.transform.scale(stone,(50,50)),330)




     

def bgdeco(first,second,third,fourth,fivth,six,charmove1,arrow1,arrowtilted1,health,timer):
    win.fill(bgcolor)
    

    win.blit(size,(0,0))
    win.blit(size_c,(charmove1.x,charmove1.y))
    

    win.blit(size_a,(first.x,first.y))
    win.blit(size_b,(second.x,second.y))
    win.blit(size_w,(third.x,third.y))
    win.blit(size_g,(fourth.x,fourth.y))
    win.blit(size_p,(fivth.x,fivth.y))
    win.blit(size_s,(six.x,six.y))
    #pygame.surface.Surface.blit(arrow,(charmove.x,charmove.y))
    
    win.blit(arrow,(arrow1.x,arrow1.y))
    win.blit(arrowtilted,(arrowtilted1.x,arrowtilted1.y))
    timer_text=timer_font.render("Timer: "+str(timer),1,(249,11,11))
    win.blit(timer_text,(1350,750))
    Health_txt=health_font.render("Health: "+  str(health),1,(249,11,11))
    win.blit(Health_txt,(10,750))
    

    pygame.display.update()

#def char_movement(key_pressed,char):
    #if key_pressed[pygame.K_LEFT] and char.x-speed>0 :
            #pygame.transform.flip(character,[char.x,char.y])
            #char.x-=speed
    #if key_pressed[pygame.K_RIGHT] and char.x+speed+char.width<width :
            
            #char.x+=speed
def wins(text):
    if(text=="YOU WIN!!!"):

        pygame.mixer.music.load(os.path.join('win sound.wav'))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load(os.path.join('lost.mp3'))
        pygame.mixer.music.play()

    wining_text=wining_font.render(text,1,(255,255,255))
    win.blit(wining_text,(width/3,height/3))
     
    pygame.display.update()
    pygame.time.delay(5000) 
    



def main(arrow):
    pygame.mixer.music.load(os.path.join('atmosphere.mp3'))
    pygame.mixer.music.play()
    first=pygame.Rect(200,-30,30,30)
    second=pygame.Rect(400,-70,50,50)
    third=pygame.Rect(600,-140,50,50)
    fourth=pygame.Rect(800,-250,50,50)
    fivth=pygame.Rect(1000,-300,60,60)
    six=pygame.Rect(1200,-380,50,50)
    charmove1=pygame.Rect(0,600,150,160)
    arrow1=pygame.Rect(charmove1.x+5,charmove1.y+15,50,80)
    
    arrowtilted1=pygame.Rect(charmove1.x+10,charmove1.y+15,50,80)
    
    health=0

    clock=pygame.time.Clock()
    
    angle=270
    key=0
    key2=0
    wining_text=""
    timer=2000
    run=True
    while run:
        
        
        clock.tick(FPS)
        speed_2=3
        timer-=1
        
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

         
        
        first.y+=speed_2
        second.y+=speed_2+3-1
        third.y+=speed_2+2-1
        fourth.y+=speed_2+4-1
        fivth.y+=speed_2+6-2
        six.y+=speed_2+7-2
        if first.y>=800 :
            first.y= -5
            
        if second.y>=800 :
            second.y= -15

        if third.y>=800 :
            third.y= -8
        if fourth.y>=800 :
            fourth.y= -9
        if fivth.y>=800 :
            fivth.y= -12
        if six.y>=800 :
            six.y= -19
        
        
        print(second.y,'second')
        
        key_pressed=pygame.key.get_pressed()
    
        if key_pressed[pygame.K_d] :
            key+=1
            arrow1.x+=weapon_vel*key
            pygame.mixer.music.load(os.path.join('arrow.mp3'))
            pygame.mixer.music.play()
        
            
            
            
        if key>=1:
            arrow1.x+=weapon_vel
            
        if arrow1.x>=width  :
            arrow1.x=5
            arrow1.y=charmove1.y+15
            
            key=0
    
        
        if key_pressed[pygame.K_RIGHT]and key_pressed[pygame.K_UP]:
            
            key2+=1
            
            arrowtilted1.x+=weapon_vel*key2
            arrowtilted1.y-=weapon_vel*key2
            pygame.mixer.music.load(os.path.join('arrow.mp3'))
            pygame.mixer.music.play()
            
        if key2>=1 :
            arrowtilted1.x+=weapon_vel
            arrowtilted1.y-=weapon_vel
        if arrowtilted1.x>=width :
            arrowtilted1.x=5
            arrowtilted1.y=charmove1.y+15
            key2=0 

        if first.colliderect(arrow1) or first.colliderect(arrowtilted1):
            pygame.mixer.music.load(os.path.join('impact.wav'))
            pygame.mixer.music.play()
            health+=10
        if second.colliderect(arrow1) or second.colliderect(arrowtilted1): 
            pygame.mixer.music.load(os.path.join('impact.wav'))
            pygame.mixer.music.play() 
            health+=20
        if third.colliderect(arrow1) or third.colliderect(arrowtilted1):
            pygame.mixer.music.load(os.path.join('impact.wav'))
            pygame.mixer.music.play()
            health+=30
        if fourth.colliderect(arrow1) or fourth.colliderect(arrowtilted1):
            pygame.mixer.music.load(os.path.join('impact.wav'))
            pygame.mixer.music.play()
            health+=40
        if fivth.colliderect(arrow1) or fivth.colliderect(arrowtilted1):
            pygame.mixer.music.load(os.path.join('impact.wav'))
            pygame.mixer.music.play()
            health+=30
        if six.colliderect(arrow1) or six.colliderect(arrowtilted1):
            pygame.mixer.music.load(os.path.join('impact.wav'))
            pygame.mixer.music.play()
            health+=0

        if health>=2010 and timer>0:
            wining_text="YOU WIN!!!"
        elif (health>=2010 and timer<=0)  or (health<2010 and timer<=0) :
            wining_text="YOU LOST!!"
            
        if wining_text!="":
            wins(wining_text)
            break
            

        

        
        
            
        

               
        
        bgdeco(first,second,third,fourth,fivth,six,charmove1,arrow1,arrowtilted1,health,timer)
        
    main()

if __name__=="__main__":

    main(arrow)