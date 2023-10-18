import streamlit as st
from multiprocessing import Process
import tkinter as tk
import os
import pandas as pd
import ScanTailorSkript
from waiting import wait
import time
import keyboard
import StopListenerSkript

root = tk.Tk()
root.withdraw()

class InterruptException (Exception):
    pass

def interrupt(p):
    p.exit()
    raise InterruptException()

def main():
    st.title('ScanTailorAuto')
    path = st.text_input('Pfad eingeben', '')
    text1 = st.write('Hier muss der Pfad des Ordners agegeben werden, in dem sich alle zu bearbeitenden Unterordner befinden ')
    text2 = st.write('> In ScanTailor müssen die richtigen Default Settings bereits eingestellt sein.')
    text3 = st.write('> Mit dem Abbruch Knopf wird die Warteschlange geleert.')
    text4= st.write('> Nach Starten des Prozesses am besten mit der Maus auf einen zweiten Bildschirm klicken')
    clicked = st.button('Start')

    if clicked:
        if path is None or path == '':
            st.error('Der Pfad darf nicht leer sein!')
        else:
            print('----------\nSTART')
            try: 
                all_folders = os.listdir(path) #alle Unterverzeichnisse 
                folders = [element for element in all_folders if os.path.isdir(os.path.join(path, element))] #Unterverzeichnisse filtern und in array folders speichern
                for x in range(len(folders)): #pfad ergänzen
                    old = folders[x]
                    folders[x] = path+"\\"+old
                count = []
                for y in range(len(folders)):
                    aktuellerPfad = folders[y]
                    countx=0
                    for path in os.listdir(aktuellerPfad):
                        countx += 1
                    count.append(count)
                status = []
                for i in range(len(folders)):
                    status.append("waiting")
                    
                df = pd.DataFrame(
                    {
                        "Ordner": folders,
                        "Anzahlt der Dateien":count,
                        "Status":status
                    }
                )
                progress_text = "aktueller Fortschritt: "
                progress_bar = st.progress(0, text = progress_text+"0 %")
                stop = st.button('Abbruch')
                übersicht = st.dataframe(
                    df,
                    hide_index=True,
                )
                time.sleep(0.5)
                #for Schleife über Unterordnern
                skript = ScanTailorSkript
                for x in range(len(df)):
                    aktuellerPfad = df.loc[x,"Ordner"]
                    df.loc[x,"Status"] = "running"
                    übersicht.dataframe(df, hide_index=True)
                    a=aktuellerPfad.split(os.sep)
                    print("Unterordner: "+a[-1])
                    #Anzahl der Dateien Zählen
                    count = df.loc[x,"Anzahl der Dateien"]
                    print("Dateien in Unterordner: "+str(count))
                    #Start ScanTailorSkript
                    error = StopListenerSkript
                    p = Process(target=skript.test(aktuellerPfad,count))
                    error.startErrorListener(p)
                    p.run()
                    wait(lambda: ScanTailorSkript.getRunFinished(), timeout_seconds = 600)
                    progress_bar.progress((x+1)/len(df), text = progress_text + str(100*round((x+1)/len(df),2))+" %")
                    df.loc[x,"Status"] = "✅"
                    übersicht.dataframe(df, hide_index=True)
                    übersicht.dataframe(df,hide_index=True)
                print("Programm Ende\n----------")

            except FileNotFoundError:
                st.error('Der gesuchte Pfad konnte nicht gefunden werden')
                exit()

            except InterruptException:
                st.error('Abbruch. Bitte erneut starten')
                st.stop()    

main()