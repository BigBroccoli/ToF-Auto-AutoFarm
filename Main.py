try:
    from time import sleep
    import os
except ImportError as e:
    raise ImportError('Missing a required library.', e)


def install(package):
    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


try:
    from pyautogui import *
except ImportError:
    install('pyautogui')
    from pyautogui import *

try:
    import PIL
except ImportError:
    install('Pillow')
    import PIL


# How many delay time seconds
start_delay_time = 1
anti_cheat_delay_time = 0.2

# get current directory
current_dir = os.getcwd()

sword_icon_image = os.path.join(current_dir, 'sword_icon.png')
challenge_icon_image = os.path.join(current_dir, 'Challenge_icon.png')
complete_icon_image = os.path.join(current_dir, 'Challenge_icon.png')
go_icon_image = os.path.join(current_dir, 'go.png')


def delay(timer):
    sleep(timer)


def anti_cheat_delay():
    sleep(anti_cheat_delay_time)


# Press and hold Alt
def press_down_key(key):
    keyDown(key)


# Stops pressing Alt
def press_up_key(key):
    keyUp(key)


# Finds sword icon by taking a screenshot then moves mouse to where the icon is found
def find_icon_location(icon_image):
    # Take screenshot
    full_screen_image = screenshot()

    # Locate icon
    loc = locateOnScreen(icon_image, full_screen_image)
    delay(1)  # Give time to find the loc
    x, y = center(loc)
    click(x, y)


def move_mouse_to_center():
    x, y = size()  # Gets size of the screen
    moveTo(x / 2, y / 2)


def main():
    print("Click into the game. Starting Script in", start_delay_time, 'sec(s).')
    delay(start_delay_time)
    press_down_key('alt')

    # Find sword icon
    find_icon_location(sword_icon_image)

    press_up_key('alt')
    anti_cheat_delay()

    # Find challenge icon
    find_icon_location(challenge_icon_image)
    anti_cheat_delay()

    # Navigate menu
    move_mouse_to_center()
    # Scroll a shit ton
    scroll(10000)

    # Find complete challenges
    find_icon_location(complete_icon_image)
    anti_cheat_delay()

    # Find Go button
    find_icon_location(go_icon_image)
    anti_cheat_delay()


main()
