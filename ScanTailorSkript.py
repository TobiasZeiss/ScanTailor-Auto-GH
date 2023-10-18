import keyboard
import mouse
import time
import os

state = True

class InterruptException (Exception):
    pass

def interrupt():
    raise InterruptException("Das Skript wurde abgebrochen")

def run (pfad, count):
    try:
        os.startfile('C:\Program Files\ScanTailor Advanced\scantailor.exe')
        time.sleep(2)
        keyboard.press_and_release('ctrl+n')
        time.sleep(0.5)
        keyboard.write(pfad)
        time.sleep(0.5)
        for x in range(5):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release('Space')
        keyboard.press_and_release('Tab')
        keyboard.press_and_release('Space')
        for x in range(6):
            keyboard.press_and_release("Tab")
            time.sleep(0.3)
        keyboard.press_and_release('Enter')
        time.sleep(0.05*count)
        
        #default Parameters Auswahl:
        #print(mouse.get_position())
        #mouse.move(-282, -1410,True)
        #time.sleep(1)
        #mouse.click('left')
        #for x in range(4):
        #    keyboard.press_and_release('down')
        #    time.sleep(0.1)
        #keyboard.press_and_release('Enter')
        #time.sleep(0.3)

        #Split Pages
        mouse.move(-151,-1326,True)
        mouse.click('left')
        time.sleep(0.1)
        mouse.click('left')
        time.sleep(0.08*count)

        #Select Content
        mouse.move(-149, -1283,True)
        mouse.click('left')
        time.sleep(0.1)
        mouse.click('left')
        time.sleep(0.15*count)

        #Margins
        mouse.move(-151,-1262)
        mouse.click('left')
        time.sleep(0.1)
        mouse.click('left')
        time.sleep(0.15*count)

        #Output
        mouse.move(-152,-1239,True)
        mouse.click('left')
        time.sleep(0.25*count)

        #Save
        keyboard.press_and_release('ctrl+s')
        time.sleep(1)
        mouse.move(-49,-1352,True) #koordinaten rausfinden --> Pfadadresse eingeben
        mouse.click('left')
        time.sleep(1)
        keyboard.write(pfad)
        keyboard.press_and_release('enter')
        time.sleep(1)
        mouse.move(-190,-1312,True) #koordinaten rausfinden --> neuer Ordner
        mouse.click('left')
        time.sleep(1)
        keyboard.write('Scantailor Projekt')
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('enter')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        time.sleep(1)
        name = pfad.split(os.sep)
        keyboard.write(name[-1])
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        mouse.move(571,-736,True) #koordinaten rausfinden --> Speichern
        mouse.click('left')
        time.sleep(1)

        #kill
        time.sleep(2)
        keyboard.press_and_release('alt+F4')
        print ("Unterordner beendet.\n ")

        #Dokument beenden, Signal an main.py schicken
        setRunFinished()


    except FileNotFoundError:
        print("ScanTailor konnte nicht gefunden werden")
        exit()

    except InterruptException:
        print("Das Skript wurde abgebrochen. Pfad: "+pfad)
        exit()

def getRunFinished ():
    return state

def setRunFinished ():
    state = True

def test(pfad, count):
    try:
        for x in range(10):
            print(x)
            time.sleep(0.2)
        setRunFinished()
    except InterruptException:
        print("Das Programm wurde abgebrochen!")
