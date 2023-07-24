import keyboard
from time import sleep
import os
from art import *
from multiprocessing import Process

os.system('color 97')
os.system('cls')

tprint('K1 Adili')
tprint('Auto Complete')

print('Add a new key in key.txt')
print('After adding a new key please wait for a few second.\n\n')
print('For example:')
print("======================================================================")
print('hw|Hello world!!')
print("When you type \"hl\" and then press space the app types \"Hello world!!\"")


if not os.path.isfile('key.txt'):
    with open('key.txt', 'w', encoding='utf8') as _:
        _.write('_hw|Hello World !!!')

def AutoComplet():
    try:
        # Read your keys from key.txt
        with open('key.txt', 'r', encoding='utf8') as f:
            lines = f.readlines()

        for line in lines:
            keys = line.split('|')
            keyboard.add_abbreviation(keys[0], keys[1].strip())

        sleep(5)
    
    except:
        print('Error ...')




if __name__ == '__main__':

    while True:
        process = Process(target=AutoComplet)
        process.start()
        process.join()

    

