import time

import keyboard
import pyautogui
import pydirectinput

inFightBool = 0
running = 0
count = 0
count_temp = 0


def restart():
    global inFightBool
    global count
    global count_temp

    rect1 = pyautogui.locateOnScreen('static/restart.png', confidence=0.9)
    if rect1 is not None:
        time.sleep(0.5)
        inFightBool = 0
        pydirectinput.press('r')
        count = count_temp
        print("已完成次数：", count)

    rect2 = pyautogui.locateOnScreen('static/in.png', confidence=0.9)
    if rect2 is not None:
        time.sleep(0.5)
        pydirectinput.press('t')

    rect3 = pyautogui.locateOnScreen('static/wep.png', confidence=0.9)
    if rect3 is not None:
        time.sleep(0.5)
        pydirectinput.press('y')

    rect4 = pyautogui.locateOnScreen('static/fight.png', confidence=0.9)
    if rect4 is not None:
        time.sleep(0.5)
        pydirectinput.press('h')
        inFightBool = 1
        count_temp = count + 1


def inFight():
    if inFightBool == 1:
        pydirectinput.keyDown('d')
        pydirectinput.keyDown('j')
    else:
        pydirectinput.keyUp('d')
        pydirectinput.keyUp('j')


print("切换到游戏界面后 长按I开始(长按O结束)")

while True:
    # rect = pyautogui.locateOnScreen('static/end.png', confidence=0.9)
    rect_get_all = pyautogui.locateOnScreen('static/allget.png', confidence=0.9)

    if keyboard.is_pressed('i'):
        running = 1

    elif keyboard.is_pressed('o'):
        running = 0
        pydirectinput.keyUp('d')
        pydirectinput.keyUp('j')
        print("! 用户主动暂停程序")
        print("已完成次数：", count)

    # 这张识别图片有问题
    # elif rect is not None:
    #     print("! 体力已耗尽，程序暂停")
    #     print("已完成次数：", count)
    #     running = 0
    #     pydirectinput.keyUp('d')
    #     pydirectinput.keyUp('j')

    elif rect_get_all is not None:
        print("! 奖励全部获取，程序暂停")
        print("已完成次数：", count)
        running = 0
        pydirectinput.keyUp('d')
        pydirectinput.keyUp('j')

    if running == 1:
        restart()
        inFight()
