import pygame
from cryptography.fernet import Fernet
import playsound
pygame.init()
win = pygame.display.set_mode((1150,700))
pygame.display.set_caption("Zakat")
bg = pygame.image.load("C:\\Users\wabal\Python Data Storage\\Data centre\kk.jpg")
bg1 = pygame.image.load("C:\\Users\wabal\Python Data Storage\\Data centre\login_bg.jpg")
button = pygame.image.load("C:\\Users\wabal\Python Data Storage\\Data centre\done button.png")
run = True
limit = 0
fps = 0
cfps = 0
sec = 0
sec1 = 0
op = 0
bBack = False
bDone = False
enter = False
speak = False

font = pygame.font.SysFont('Agency FB',25)
big  = pygame.font.SysFont('Agency FB',50)
title = font.render("Zakat Maneger",True,(255,165,0))
username = font.render("Username :",True,(0,0,0))
password = font.render("Password :",True,(0,0,0))
cal = font.render("Zakat Calculator",True,(0,0,0))
give = font.render("Zakat Given",True,(0,0,0))
gold = big.render("Self distruct compelete this section will never be public again",True,(255,0,0))
fcur = font.render("Forgein Curreny",True,(0,0,0))
cur = font.render("Local Curreny",True,(0,0,0))
hrent = font.render("House Rent",True,(0,0,0))
log = font.render("Login",True,(255,100,0))
k22 = font.render("21K Gold",True,(255,215,0))
k23 = font.render("22K Gold",True,(255,215,0))
k24 = font.render("24k Gold",True,(255,215,0))
rate = font.render("Rates",True,(255,0,0))
weight = font.render("Weight",True,(255,0,0))
gram = font.render("/Gram",True,(50,255,50))
done = font.render("Done",True,(0,0,0))
back = font.render("Back",True,(0,0,0))
ex = font.render("Exchange Rate",True,(255,0,0))
pertime = font.render("Number of months",True,(255,0,0))
val  = font.render("Amount",True,(255,0,0))
re = font.render("remaining",True,(255,0,0))
pygame.mouse.set_visible(1)
count = 30
count2 = 30
count3 = 30
count4 = 30
count5 = 30
date = 0
olddate = 0
user = False
word = False
userName = ""
passcode = ""
pass_show = ""
login = False
logbutton = False
listen = ""

def drawpass(user,word,logbutton):
    box1 = font.render(userName,True,(255,255,255))
    box2 = font.render(pass_show,True,(255,255,255))
    win.fill((145,50,200))
    win.blit(bg1,((0,0)))
    win.blit(title,((50,50)))
    win.blit(username,((400,300)))
    win.blit(password,((400,400)))
    win.blit(box1,((500,303)))
    win.blit(box2,((501,405)))
    if user == True:
        pygame.draw.rect(win,((255,0,0)),(500,300,200,20),1)
    else:
        pygame.draw.rect(win,((255,255,0)),(500,300,200,20),1)
    if word == True:
        pygame.draw.rect(win,((255,0,0)),(500,400,200,20),1)
    else:
        pygame.draw.rect(win,((255,255,0)),(500,400,200,20),1)
        
    if logbutton == True:
        pygame.draw.rect(win,((255,255,255)),(550,500,50,30),1)
        win.blit(log,((552,505)))
    pygame.display.update()
while run:
    click1,click2,click3 = pygame.mouse.get_pressed()
    if click1 == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        if x >= 500 and x <= 700:
            if y >= 300 and y <= 320:
                user = True
                pygame.mouse.set_visible(0)
        if x >= 500 and x <= 700:
            if y >= 400 and y <= 420:
                word = True
                pygame.mouse.set_visible(0)
        if x >= 550 and x <= 600:
            if y >= 500 and y <= 530:
                if logbutton == True:
                    search = "C:\\Users\wabal\Python Data Storage\\Data centre\K45"+userName +".txt"
                    info = open(search,"rb")
                    key = info.readline()
                    name = info.readline()
                    real = info.readline()
                    dob = info.readline()
                    info.close()

                    info = open(search,"wb")
                    info.close()
                    
                    f = Fernet(key)
                    name = name = f.decrypt(name)
                    name = name.decode()

                    f = Fernet(key)
                    real = real = f.decrypt(real)
                    real = real.decode()

                    f = Fernet(key)
                    dob = dob = f.decrypt(dob)
                    dob = dob.decode()

                    name1 = name
                    real1 = real
                    dob1 = dob

                    from cryptography.fernet import Fernet

                    key = key = Fernet.generate_key()

                    name1 = name1.encode()
                    f = Fernet(key)
                    name1 = f.encrypt(name1)

                    real1 = real1.encode()
                    f = Fernet(key)
                    real1 = f.encrypt(real1)

                    dob1 = dob1.encode()
                    f = Fernet(key)
                    dob1 = f.encrypt(dob1)

                    info = open(search,"ab")
                    info.write(key)
                    info.write(b'\n')
                    info.write(name1)
                    info.write(b'\n')
                    info.write(real1)
                    info.write(b'\n')
                    info.write(dob1)

                    info.close()

                    if real == passcode:
                        login = True
                    else:
                        login = False
                    run = False
                
    pygame.time.delay(limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                word = False
                user = False
                pygame.mouse.set_visible(1)
            if user == True and len(userName) < 20:
                userName += event.unicode
            if word == True and len(passcode) < 27:
                passcode += event.unicode
                pass_show += "*"
            if event.key == pygame.K_BACKSPACE and user == True:
                userName = userName[0:-2]
            if event.key == pygame.K_BACKSPACE and word == True:
                passcode = passcode[0:-2]
                pass_show = pass_show[0:-2]

    if len(userName) >= 5 and len(passcode) >= 5:
        logbutton = True
    else:
        logbutton = False
                
    import time
    date = str(time.ctime(time.time()))
    date = date[17:20]
    if date == olddate:
        cfps += 1
    if date != olddate:
        olddate = date
        fps = cfps
        cfps = 0
        if fps < 30:
            limit -= 1
        if fps > 30:
            limit += 1

    drawpass(user,word,logbutton)
#---------------------------------------------------------------___________________________------------------------------------------------------------------------
limit = 50
def draw(bDone,bBack):
    win.blit(title,((50,50)))
    if bDone == True:
        win.blit(button,((190,580)))
        win.blit(done,((218,592)))
    elif bBack == True:
        win.blit(button,((190,580)))
        win.blit(back,((218,592)))
    pygame.display.update()
    win.fill((0,0,0))
    win.blit(bg,((0,0)))

def Zakat_Gold(op,r22,r23,r24,w22,w23,w24,first,speak,w,r,listen,enter,bBack,bDone):
    if enter == True:
        bBack = True
        bDone = False
        if w[0] == 1:
            w22 = int(listen)
        if w[1] == 1:
            w23 = int(listen)
        if w[2] == 1:
            w24 = int(listen)
        if r[0] == 1 and int(listen) >= 1000:
            r22 = int(listen)
        if r[1] == 1 and int(listen) >= 1000:
            r23 = int(listen)
        if r[2] == 1 and int(listen) >= 1000:
            r24 = int(listen)
        w = [0,0,0]
        r = [0,0,0]
        listen = ""
        enter = False
    if first == False:
        click1 = False
        read = ["","",""]
        l = 0
        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\Gold.txt","r")
        for i in range(0,3):
            read[i] = file.readline()
            if "\n" in read[i]:
                l = len(read[i])
                read[i] = read[i][0:l-1]
        file.close()
        r22 = int(read[0])
        r23 = int(read[1])
        r24 = int(read[2])
    else:
        click1,click2,click3 = pygame.mouse.get_pressed()
    if click1 == True and first == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        pygame.time.delay(300)
        if x >= 100 and x <= 300 and y >= 200 and y <= 250:
            w[0] = 1
            speak = True
            listen = str(w22)
            pygame.mouse.set_visible(0)
        if x >= 450 and x <= 650 and y >= 200 and y <= 250:
            w[1] = 1
            speak = True
            listen = str(w23)
            pygame.mouse.set_visible(0)
        if x >= 800 and x <= 1000 and y >= 200 and y <= 250:
            w[2] = 1
            speak = True
            listen = str(w24)
            pygame.mouse.set_visible(0)
        if x >= 150 and x <= 250 and y >= 125 and y <= 150:
            r[0] = 1
            speak = True
            listen = str(r22)
            pygame.mouse.set_visible(0)
        if x >= 500 and x <= 600 and y >= 125 and y <= 150:
            r[1] = 1
            speak = True
            listen = str(r23)
            pygame.mouse.set_visible(0)
        if x >= 850 and x <= 950 and y >= 125 and y <= 150:
            r[2] = 1
            speak = True
            listen = str(r24)
            pygame.mouse.set_visible(0)
        
    return r22,r23,r24,w22,w23,w24,speak,w,r,listen,enter,bBack,bDone
def Zakat_Give(bBack,bDone,speak,listen,enter,c,amount,first):
    if first == False:
        click1 = False
        first = True
    else:
        click1,click2,click3 = pygame.mouse.get_pressed()
    if enter == True and c == 1: 
        amount = int(listen)
        c = 0
        speak = False
        bBack = True
        bDone = False
        enter = False
    if click1 == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        pygame.time.delay(300)
        if x >= 450 and x <= 650 and y >= 200 and y <= 250:
            # VAL
            c = 1
            speak = True
            listen = str(amount)
            pygame.mouse.set_visible(0)
    return bBack,bDone,speak,listen,enter,c,amount,first
def Zakat_hrent(bBack,bDone,speak,listen,enter,c,perent,rent,first):
    if first == False:
        click1 = False
        first = True
    else:
        click1,click2,click3 = pygame.mouse.get_pressed()
    if enter == True and c[1] == 1: 
        rent = int(listen)
        c[1] = 0
        speak = False
        bBack = True
        bDone = False
        enter = False
    elif enter == True and c[0] == 1:
        perent = int(listen)
        c[0] = 0
        speak = False
        bBack = True
        bDone = False
        enter = False
    if click1 == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        pygame.time.delay(300)
        if x >= 450 and x <= 650 and y >= 200 and y <= 250:
            # VAL
            c[1] = 1
            speak = True
            listen = str(rent)
            pygame.mouse.set_visible(0)
        elif x >= 500 and x <= 600 and y >= 125 and y <= 150:
            # Ex
            c[0] = 1
            speak = True
            listen = str(perent)
            pygame.mouse.set_visible(0)
    return bBack,bDone,speak,listen,enter,c,perent,rent,first
def Zakat_cur(bBack,bDone,speak,listen,enter,lcur,first,oldcur,c):
    if first == False:
        click1 = False
        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\mopak.txt","r")
        oldcur = file.readline()
        file.close()
        l = 0
        first = True
        if "\n" in oldcur:
            l = len(oldcur)
            oldcur = oldcur[0:l-1]
    click1,click2,click3 = pygame.mouse.get_pressed()
    if click1 == True and first == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        pygame.time.delay(300)
        if x >= 450 and x <= 650 and y >= 200 and y <= 250:
            # VAL
            c = 1
            speak = True
            listen = str(lcur)
            pygame.mouse.set_visible(0)
    if enter == True and c == 1: 
        lcur = int(listen)
        c = 0
        speak = False
        bBack = True
        bDone = False
        enter = False
    return bBack,bDone,speak,listen,enter,lcur,first,oldcur,c
def Zakat_Fcur(bBack,bDone,speak,listen,enter,c,erate,vcur,first,oldfcur):
    if first == False:
        click1 = False
        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\ecur.txt","r")
        erate = file.readline()
        oldfcur = file.readline()
        file.close()
        l = 0
        if "\n" in erate:
            l = len(erate)
            erate = erate[0:l-1]
        if "\n" in oldfcur:
            l = len(oldfcur)
            oldfcur = oldfcur[0:l-1]
        first = True
    else:
        click1,click2,click3 = pygame.mouse.get_pressed()
    if enter == True and c[1] == 1: 
        vcur = int(listen)
        c[1] = 0
        speak = False
        bBack = True
        bDone = False
        enter = False
    elif enter == True and c[0] == 1:
        erate = float(listen)
        c[0] = 0
        speak = False
        bBack = True
        bDone = False
        enter = False
    if click1 == True:
        pos = pygame.mouse.get_pos()
        line = str(pos)
        coma = int(line.find(","))
        fbracket = int(line.find("("))
        lbracket = int(line.find(")"))
        x = int(line[fbracket + 1:coma])
        y = int(line[coma+2:lbracket])
        pygame.time.delay(300)
        if x >= 450 and x <= 650 and y >= 200 and y <= 250:
            # VAL
            c[1] = 1
            speak = True
            listen = str(vcur)
            pygame.mouse.set_visible(0)
        elif x >= 500 and x <= 600 and y >= 125 and y <= 150:
            # Ex
            c[0] = 1
            speak = True
            listen = str(erate)
            pygame.mouse.set_visible(0)
    return (bBack,bDone,speak,listen,enter,c,erate,vcur,first,oldfcur)
def frams(fps,cfps,limit,sec,sec1):
    import time
    sec = time.ctime()
    if sec !=  sec1:
        fps = cfps
        cfps = 0
        sec1 = sec
    else:
        cfps += 1
        
    if fps > 10:
        limit += 1
    if fps < 10:
        limit -= 1
    info = font.render(str(fps),True,(0,0,0))
    win.blit(info,((0,0)))
    
    return fps,cfps,limit,sec,sec1
run = True
if login == True:
    win.fill((255,0,0))
    pygame.display.update()
    playsound.playsound("C:\\Users\wabal\Python Data Storage\\Data centre\psa.mp3")
    file = open("C:\\Users\wabal\Python Data Storage\\Data centre\master.txt","r")
    master = file.readline()
    file.close()
    while run:
        pygame.time.delay(limit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and speak == True:
                if event.key == pygame.K_RETURN:
                    enter = True
                    listen = float(listen)
                    pygame.mouse.set_visible(1)
                if  "0" in event.unicode or "1" in event.unicode or  "2" in event.unicode or "." in event.unicode or "3" in event.unicode or "4" in event.unicode or "5" in event.unicode or "6" in event.unicode or "7" in event.unicode or "8" in event.unicode or "9" in event.unicode:
                    if len(listen) == 1 and listen == "0":
                        listen = event.unicode
                    elif len(listen) < 8:
                        listen += event.unicode
                if event.key == pygame.K_BACKSPACE :
                    listen = listen[0:-1]
                    if len(listen) == 0:
                        listen = "0"


        
        click1,click2,click3 = pygame.mouse.get_pressed()
        if click1 == True:
            pos = pygame.mouse.get_pos()
            line = str(pos)
            coma = int(line.find(","))
            fbracket = int(line.find("("))
            lbracket = int(line.find(")"))
            x = int(line[fbracket + 1:coma])
            y = int(line[coma+2:lbracket])
            pygame.time.delay(100)
            if x >= 100 and x <= 300 and y >= 200 and y <= 250 and op == 0:
                op =1
            elif x >= 800 and x <= 1000 and y >= 200 and y <= 250 and op == 0:
                op = 6
                amount = 0
                c = 0
                first = False
                speak = False
                bBack = False
                bDone = False
            elif x >= 100 and x <= 300 and y >= 200 and y <= 250 and op == 1:
                #Gold
                op = 3
                r22 = 0
                r23 = 0
                r24 = 0
                w22 = 0
                w23 = 0
                w24 = 0
                r = [0,0,0]
                w = [0,0,0]
                first = False
                speak = False
                bBack = False
                bDone = False
            elif x >= 800 and x <= 1000 and y >= 200 and y <= 250 and op == 1:
                #cur
                op = 4
                lcur = 0
                oldcur = 0
                c = 0
                bBack = False
                bDone = False
                first = False
                speak = False
            elif x >= 450 and x <= 650 and y >= 200 and y <= 400 and op == 1:
                #fcur
                op = 2
                erate = float(0)
                vcur = 0
                first = False
                bBack = False
                bDone = False
                speak = False
                oldfcur = 0
                c = [0,0]
            elif x >= 450 and x <= 650 and y >= 400 and y <= 600 and op == 1:
                #hrent
                c = [0,0]
                op = 5
                rent = 0
                perent = 0
                bBack = False
                bDone = False
                first = False
                speak = False
            elif x >= 195 and x <= 282 and y >= 585 and y <= 618 :
                if bDone == True:
                    if op == 0:
                        pygame.quit()
                        quit()
                elif bBack == True:
                    read = ["","",""]
                    if op == 6:
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\zakatmaster.txt","r")
                        seeop = file.read()
                        file.close()
                        khanwrites = str(sec)+"*"+str(name)+"*"+str(amount)
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\zakatmaster.txt","w")
                        file.write(seeop)
                        file.write("\n")
                        file.write(khanwrites)
                        file.close()
                        master = float(master) - amount
                        file  = open("C:\\Users\wabal\Python Data Storage\\Data centre\master.txt","w")
                        file.write(str(master))
                        file.close()
                        bBack = False
                        bDone = True
                        op = 0
                    if op == 1:
                        file  = open("C:\\Users\wabal\Python Data Storage\\Data centre\master.txt","w")
                        file.write(str(master))
                        file.close()
                        bBack = False
                        bDone = True
                        op = 0
                    if op == 4:
                        master = float(master) + float(int(lcur)*0.025)
                        lcur += int(oldcur)
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\mopak.txt","w")
                        file.write(str(lcur))
                        file.close()
                        op = 1
                    if op == 2:
                        vcur = float(float(vcur) * float(erate))
                        master = float(master) + float(float(vcur)*0.025)
                        vcur += float(oldfcur)
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\ecur.txt","w")
                        file.write(str(erate))
                        file.write("\n")
                        file.write(str(vcur))
                        file.close()
                        op = 1
                    if op == 5:
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\hrent.txt","r")
                        oldrent = file.readline()
                        file.close()
                        rent = rent * perent
                        master = float(master) + float(int(rent)*0.025)
                        rent += int(oldrent)
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\hrent.txt","w")
                        file.write(str(rent))
                        file.close()
                        op = 1
                    if op == 3:
                        master = float(master) + float(float(w22 * r22)*0.025)
                        master = float(master) + float(float(w23 * r23)*0.025)
                        master = float(master) + float(float(w24 * r24)*0.025)
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\pold.txt","r")
                        for i in range(0,3):
                            read[i] = file.readline()
                            if "\n" in read[i]:
                                read[i] = read[i][0:len(read[i])-1]
                        file.close
                        p22 = int(read[0])
                        p23 = int(read[1])
                        p24 = int(read[2])
                        if w22 > 0:
                            p22 += (w22 * r22)
                        if w23 > 0:
                            p23 += (w23 * r23)
                        if w24 > 0:
                            p24 += (w24 * r24)
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\pold.txt","w")
                        file.write(str(p22))
                        file.write("\n")
                        file.write(str(p23))
                        file.write("\n")
                        file.write(str(p24))
                        file.close()
                        file = open("C:\\Users\wabal\Python Data Storage\\Data centre\Gold.txt","w")
                        file.write(str(r22))
                        file.write("\n")
                        file.write(str(r23))
                        file.write("\n")
                        file.write(str(r24))
                        file.close()
                        op = 1
            
            
        draw(bDone,bBack)
        if op == 0:
            win.blit(cal,((131,220)))
            win.blit(give,((850,220)))
            pygame.draw.rect(win,((255,255,0)),((100,200,200,50)),2)
            pygame.draw.rect(win,((255,255,0)),((800,200,200,50)),2)
        elif op ==1:
            pygame.mouse.set_visible(0)
            win.fill((0,0,0))
            win.blit(gold,((20,220)))
        elif op == 2:
            serate = font.render(str(erate),True,(10,10,10))
            svcur = big.render(str(vcur),True,(255,255,255))
            slisten = font.render(str(listen),True,(255,0,0))
            blisten = big.render(str(listen),True,(255,0,0))
            pygame.draw.rect(win,((255,255,0)),(450,200,200,50),2)
            pygame.draw.rect(win,((0,0,0)),((500,125,100,25)),1)
            win.blit(ex,((350,125)))
            win.blit(val,((350,215)))
            if c[0] == 0:
                win.blit(serate,((510,130)))
            else:
                win.blit(slisten,((510,130)))
            if c[1] == 0:
                win.blit(svcur, ((485,210)))
            else:
                win.blit(blisten,((485,210)))
            bBack,bDone,speak,listen,enter,c,erate,vcur,first,oldfcur = Zakat_Fcur(bBack,bDone,speak,listen,enter,c,erate,vcur,first,oldfcur)
        elif op == 3:
            sr22 = font.render(str(r22),True,(255,255,255))
            sr23 = font.render(str(r23),True,(255,255,255))
            sr24 = font.render(str(r24),True,(255,255,255))
            sw22 = big.render(str(w22),True,(10,10,10))
            sw23 = big.render(str(w23),True,(10,10,10))
            sw24 = big.render(str(w24),True,(10,10,10))
            slisten = font.render(str(listen),True,(255,0,0))
            blisten = big.render(str(listen),True,(255,0,0))
            pygame.draw.rect(win,((255,255,0)),((100,200,200,50)),2)
            pygame.draw.rect(win,((255,255,0)),((800,200,200,50)),2)
            pygame.draw.rect(win,((255,255,0)),((450,200,200,50)),2)
            pygame.draw.rect(win,((0,0,0)),((150,125,100,25)),1)
            pygame.draw.rect(win,((0,0,0)),((850,125,100,25)),1)
            pygame.draw.rect(win,((0,0,0)),((500,125,100,25)),1)
            win.blit(k22,((160,300)))
            win.blit(k23,((510,300)))
            win.blit(k24,((860,300)))
            win.blit(weight,((20,225)))
            win.blit(rate,((20,125)))
            win.blit(gram,((310,225)))
            win.blit(gram,((1010,225)))
            win.blit(gram,((660,225)))
            win.blit(gram,((260,130)))
            win.blit(gram,((960,130)))
            win.blit(gram,((610,130)))
            if r[0] == 1:
                win.blit(slisten,((160,130)))
            else:
                win.blit(sr22,((160,130)))
            if r[1] == 1:
                win.blit(slisten,((510,130)))
            else:
                win.blit(sr23,((510,130)))
            if r[2] == 1:
                win.blit(slisten,((860,130)))
            else:
                win.blit(sr24,((860,130)))
            if w[0] == 1:
                win.blit(blisten,((110,215)))
            else:
                win.blit(sw22,((110,215)))
            if w[1] == 1:
                win.blit(blisten,((460,215)))
            else:
                win.blit(sw23,((460,215)))
            if w[2] == 1:
                win.blit(blisten,((810,215)))
            else:
                win.blit(sw24,((810,215)))
            r22,r23,r24,w22,w23,w24,speak,w,r,listen,enter,bBack,bDone = Zakat_Gold(op,r22,r23,r24,w22,w23,w24,first,speak,w,r,listen,enter,bBack,bDone)
            first = True
        elif op == 4:
            scur = big.render(str(lcur),True,(255,255,255))
            blisten = big.render(str(listen),True,(255,0,0))
            pygame.draw.rect(win,((255,255,0)),(450,200,200,50),2)
            win.blit(val,((350,215)))
            if c == 0:
                win.blit(scur, ((485,210)))
            else:
                win.blit(blisten,((485,210)))
            bBack,bDone,speak,listen,enter,lcur,first,oldcur,c = Zakat_cur(bBack,bDone,speak,listen,enter,lcur,first,oldcur,c)
        elif op == 5:
            sperent = font.render(str(perent),True,(10,10,10))
            srent = big.render(str(rent),True,(255,255,255))
            slisten = font.render(str(listen),True,(255,0,0))
            blisten = big.render(str(listen),True,(255,0,0))
            pygame.draw.rect(win,((255,255,0)),(450,200,200,50),2)
            pygame.draw.rect(win,((0,0,0)),((500,125,100,25)),1)
            win.blit(pertime,((330,125)))
            win.blit(val,((350,215)))
            if c[0] == 0:
                win.blit(sperent,((510,130)))
            else:
                win.blit(slisten,((510,130)))
            if c[1] == 0:
                win.blit(srent, ((485,210)))
            else:
                win.blit(blisten,((485,210)))
            bBack,bDone,speak,listen,enter,c,perent,rent,first = Zakat_hrent(bBack,bDone,speak,listen,enter,c,perent,rent,first)
        elif op == 6:
            samount = big.render(str(amount),True,(255,255,255))
            blisten = big.render(str(listen),True,(255,0,0))
            smaster = big.render(str(master),True,(255,255,255))
            pygame.draw.rect(win,((255,255,0)),(450,200,200,50),2)
            win.blit(val,((350,215)))
            win.blit(re,((350,550)))
            win.blit(smaster,((350,600)))
            if c == 0:
                win.blit(samount, ((485,210)))
            else:
                win.blit(blisten,((485,210)))
            bBack,bDone,speak,listen,enter,c,amount,first = Zakat_Give(bBack,bDone,speak,listen,enter,c,amount,first)
        fps,cfps,limit,sec,sec1 = frams(fps,cfps,limit,sec,sec1)
pygame.quit()
