import pygame
import pyautogui
import time
import numpy as np
import subprocess

DEAD_ZONE_LEFT = 0.05  # 0-1
DEAD_ZONE_RIGHT = 0.2  # 0-1
CURSOR_INDEX = 1.5
CURSOR_SPEED = 20
SCROLL_SPEED = 0.3

PAD_BUTTON_A         =  0
PAD_BUTTON_B         =  1
PAD_BUTTON_X         =  2
PAD_BUTTON_Y         =  3
PAD_BUTTON_L1        =  4
PAD_BUTTON_R1        =  5
PAD_BUTTON_SELECT    =  6
PAD_BUTTON_START     =  7
PAD_BUTTON_HART      =  8
PAD_BUTTON_JOY_LEFT  =  9
PAD_BUTTON_JOY_RIGHT = 10
PAD_HAT = 0
PAD_AXIS_LEFT_HORIZONTAL  = 0
PAD_AXIS_LEFT_VERTICAL    = 1
PAD_AXIS_L2               = 2
PAD_AXIS_RIGHT_HORIZONTAL = 3
PAD_AXIS_RIGHT_VERTICAL   = 4
PAD_AXIS_R2               = 5

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

pygame.init()
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

pygame.event.set_allowed([pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP])

scroll_sum = 0

while True:
    axes_left = [joy.get_axis(0), joy.get_axis(1)]
    for i in range(len(axes_left)):
        axes_left[i] = axes_left[i] if np.abs(axes_left[i]) > DEAD_ZONE_LEFT else 0
        axes_left[i] = np.sign(axes_left[i]) * np.abs(axes_left[i]) ** CURSOR_INDEX
    pyautogui.move(
        int(axes_left[0] * CURSOR_SPEED),
        int(axes_left[1] * CURSOR_SPEED)
    )
    
    axis_right_vertical = joy.get_axis(4)
    if np.abs(axis_right_vertical) < DEAD_ZONE_RIGHT:
        axis_right_vertical = 0
    scroll_sum += axis_right_vertical * SCROLL_SPEED
    if np.abs(scroll_sum) > 1:
        pyautogui.scroll(-1 * int(np.sign(scroll_sum)))
        scroll_sum -= np.sign(scroll_sum)
        
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.JOYBUTTONDOWN:
            if e.button == PAD_BUTTON_A:
                pyautogui.mouseDown()
            if e.button == PAD_BUTTON_B:
                pyautogui.mouseDown(button='right')
            if e.button == PAD_BUTTON_X:
                pyautogui.hotkey('ctrl', 'w')
            if e.button == PAD_BUTTON_SELECT:
                subprocess.Popen('onboard')
        elif e.type == pygame.JOYBUTTONUP:
            if e.button == PAD_BUTTON_A:
                pyautogui.mouseUp()
            if e.button == PAD_BUTTON_B:
                pyautogui.mouseUp(button='right')
        elif e.type == pygame.JOYHATMOTION:
            if e.value[0] < 0:
                pyautogui.hotkey('alt', 'left')
            if e.value[0] > 0:
                pyautogui.hotkey('alt', 'right')

    time.sleep(0.01)