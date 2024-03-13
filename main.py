import webbrowser
import time
import pyautogui

webbrowser.open_new('https://foundation.app/@jeffzyu/stilldreaming/3')
time.sleep(5)

while True:
    webbrowser.open_new_tab('https://foundation.app/@jeffzyu/stilldreaming/3')
    time.sleep(3)
    pyautogui.hotkey('command', 'w')
    time.sleep(3)
    
	