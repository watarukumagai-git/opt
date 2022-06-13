#coding: utf-8 
import re
import os
from os import path
import pyautogui as pa
import time

def get_status():
    # get cursor position and size of screen
    print(pa.position())
    print(pa.size())


def move_cursor():
    # move cursor to absolute position fron now in screen
    pa.moveTo(500, 500, duration=1)
    pa.mouseUp(x=300, y=300, button="left")
    pa.mouseDown(x=700, y=700, button="left")


def crick():
    # right/left click and double click
    pa.click(x=700, y=700, clicks=1, interval=1, button="left")
    pa.rightClick(x=700, y=700)
    pa.doubleClick()


def send_key():
    # write string and press key
    pa.write("Hello world!", interval=0.25)
    pa.press("a")
    pa.hotkey("ctrl", "a")

def msg():
    pa.alert(text='This is Test.', title='Test', button='OK')
    pa.prompt(text='This is Prompt.', title='Prompt', default='')

if __name__ == "__main__":
    get_status()
    #time.sleep(1)
    msg()
