import keyboard
import time

# ------- CONFIGURATION -------
#
KeyToHold = 'F6' # Example: KeyToHold = 'F6'
KeyToSpam = ' ' # Example: KeyToSpam = ' ' (spams spacebar)
DelayInSeconds = 0.01 # Example: DelayInSeconds = 0.01
#
# ------- CONFIGURATION -------

try:
    while True:
        while keyboard.is_pressed(KeyToHold):
            keyboard.send(' ')
            print(f"{KeyToHold} is being held")
            time.sleep(DelayInSeconds)
except:
    pass
finally:
    keyboard.unhook_all()

# keep window alive if program stops
k=input("The program has failed. This could be because you entered an invalid number for the delay, entered an invalid key, or the key is not surrounded by two apostrophes. Press return to exit.")
