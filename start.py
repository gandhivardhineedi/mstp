from time import sleep 
from subprocess import call 
import os
def clear(): 
    _ = call('clear' if os.name =='posix' else 'cls')  
def user(name):
    if not name:
        return 'enter name'
    print("loading")
    for i in range(10):
        sleep(3)
        print('.',end=' ')
    clear()
    print('game stats in :')
    for i in range(1,3,-1):
        print(i)
        clear()
    return 'welcome'+name