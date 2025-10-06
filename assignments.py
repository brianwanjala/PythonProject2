from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)

t1=Hello()
sleep(.2)
t2=Hi()
t1.start()
t2.start()
t1.join()
t2.join()
print('Bye')