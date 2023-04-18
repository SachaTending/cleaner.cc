#!/bin/python3
"""
Textwall.cc cleaner by TendingStream73
Recommended settings:
Zoom: 91%
Black theme
"""
__version__ = 1.0
__author__ = "TendingStream73"
import pyautogui, time

print("textwall.cc cleaner, i will spam with cords)")
s: list[int, int, int] = [0, 0, 0]
loc = 0
t = ""
name = ""
def clean():
    global loc, s
    lastx = 0
    a = 0
    cont = False
    while True:
        for i in pyautogui.locateAllOnScreen(t):
            x, y = pyautogui.center(i)
            ac = y
            print(f"Pass {a}: Cords:", x, y)
            if y != lastx:
                lastx = y
                s[loc] = x
                loc += 1
                if loc > 2: loc = 0
                pyautogui.click(x, y, _pause=False)
            if s == [x, x, x]:
                loc = 0
                s = [0, 0, 0]
                pyautogui.click(x-2, y-2, _pause=False)
            pyautogui.write(' ', interval=0.001, _pause = False)
            time.sleep(0.03)
        if pyautogui.locateCenterOnScreen(t) == None:
            print(f"Trying to find {name}...")
            for b in range(5):
                for _ in range(10): pyautogui.press("right")
                if pyautogui.locateCenterOnScreen(t) != None:
                    print(f"Found {name}: Try: {b}, Direction: right")
                    cont = True
                    break
            if cont:
                cont = False
                continue
            else:
                print(f"{name} not found")
                break
        a += 1

stuff: list[dict[str, str]] = [
    {
        'name': 'fire',
        'target': 'target.png'
    },
    {
        'name': 'eight',
        'target': 'eight.png'
    }
]
for i in stuff:
    name = i['name']
    t = i['target']
    print(f"Name: {name}, Image: {t}")
    clean()
print("Cleanup is done")
