import winsound
import os
import sys
import time
def GetSoundName():
    return "SudnoBoris.wav"
def PlaySound():
    flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    winsound.PlaySound(GetSoundName(), flags)
if __name__ == "__main__":
    PlaySound()
    zzz = input("Please Write 'Exit' to Close This Python Script: ")
    if zzz == "Exit":
        exit(445)
    else:
        print("FAILED!!!")
        while True:
            time.sleep(0.7)
