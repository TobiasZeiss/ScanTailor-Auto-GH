import keyboard

class InterruptException (Exception):
    pass

def stop(p):
    print("Abbruch")
    p.kill()
    raise InterruptException
    
def startErrorListener(p):
    keyboard.add_hotkey('a', stop, args=(p))
    #keyboard.wait('esc')
    