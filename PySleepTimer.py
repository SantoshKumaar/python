"""
PysleepTimer version 1.0.0
Python program to accept seconds as integer value, put windows computer to sleep after interval.
pyautogui - to call keybind shortcuts.
easygui - to call dialogue box. 
time - to wait for a given interval of time.

Requirements 
     Microsoft Windows 32 or 64 bit OS.

Issues 
    time.sleep() rejecting values over 60.
    for loop used to overcome said issue.
"""
import pyautogui
import easygui
import time
interval = easygui.enterbox("Enter time interval in seconds")
i = int(interval)
def sleep(n):
    for i in range(n):
        time.sleep(1)
sleep(i)
pyautogui.hotkey ('win', 'd' )
pyautogui.hotkey ('alt', 'f4')
pyautogui.hotkey ('left')
pyautogui.hotkey ('enter')

