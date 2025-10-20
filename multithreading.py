import threading
import time
def walking_dog(f):
    time.sleep(4)
    print(f"You finished walking {f}")

def taking_out_trash():
    print(f'You got out the trash')
    time.sleep(3)
def cooking():
    print(f"Cooking is done")
    time.sleep(2)

walking = threading.Thread(target= walking_dog, args=("John",))
walking.start()

trash = threading.Thread(target= taking_out_trash())
trash.start()

cook = threading.Thread(target= cooking())
cook.start()

walking.join()
print("Goodbye")


