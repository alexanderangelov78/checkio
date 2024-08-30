import pyautogui
import time

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pridnt_hi (name):
    # U
    # rse a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Pressдна
# the green button in the gutter to\


if __name__ == '__main__':
    print('PyCharm')

for x in range(310, 600, 10):
    for y in range(210,720, 10):
        print (x,y)
        pyautogui.moveTo(x, y)
        time.sleep(100)
        pyautogui.click()
        pyautogui.scroll(103)
        time.sleep(100)
pyautogui.moveTo(1000,1000)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
