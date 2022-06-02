import pyautogui as pyau
import time as ti
from random import randint, random, uniform

GIRunTime = True

def vs_code():
    pyau.press('win')
    ti.sleep(0.35)
    pyau.write('vs code')
    ti.sleep(0.35)
    pyau.press('ente')

def num_gussing():
    Low = int(input('the smallest possible number:'))
    High = int(input('the largest possible number:'))
    NumToGuess = randint(Low,High)


    runG = True

    while runG == True:
     x = int(input('witch number is it:'))
     if x > NumToGuess:
      print('lower')
     elif x < NumToGuess:
      print('higher')
     elif x == NumToGuess:
      print('you won')
      runG = False    

def discord():
    pyau.press('win')
    ti.sleep(0.35)
    pyau.write('discord')
    ti.sleep(0.35)
    pyau.press('enter')

def osu():
    pyau.press('win')
    pyau.write('osu')
    pyau.press('enter')

def open_browser():
    pyau.press('win')
    ti.sleep(0.5)
    pyau.write('chrome')
    ti.sleep(0.35)
    pyau.press('enter')

def newtab():
    pyau.moveTo(x=1898, y=73)
    ti.sleep(0.5)
    pyau.click()
    ti.sleep(0.5)
    pyau.moveTo(x=1721, y=103)
    pyau.click()

def search(search):
    pyau.press('win')
    pyau.write(search)
    pyau.press('enter')

def youtube():
    open_browser()
    newtab()
    ti.sleep(0.35)
    pyau.write('youtube.com')
    pyau.press('enter')

def spotify():
    open_browser()
    newtab()
    ti.sleep(0.35)
    pyau.write('open.spotify.com')
    pyau.press('enter')

while GIRunTime == True:
    print('1. VS_Code')
    print('2. Discord')
    print('3. Osu')
    print('4. Spotify')
    print('5. open_browser')
    print('6. Guess a number')
    print('7. YT')
    print('Search == Search on the destop env')
    print('bye == stops the programe')
    print('make your choice!!!!!')

    user_input = input()
    if user_input == '1':
        vs_code()
    elif user_input == '2':
        discord()
    elif user_input == '3':
        osu()
    elif user_input == '4':
        spotify()
    elif user_input == '5':
        open_browser()
    elif user_input == '6':
        num_gussing()
    elif user_input == '7':
        youtube()
    elif user_input == 'search':
        print('what you search for')
        searche = input()
        search(searche)
    elif user_input == 'bye':
        break

print('bye')