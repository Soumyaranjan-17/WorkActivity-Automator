# === LOW-LEVEL KEY UTILITIES ===
import time
import sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

def press_key_combination(*keys):
    for key in keys:
        keyboard.press(key)
    time.sleep(0.1)
    for key in reversed(keys):
        keyboard.release(key)
    time.sleep(0.3)

def press_down_arrow():
    keyboard.press(Key.down)
    time.sleep(0.05)
    keyboard.release(Key.down)
    print("      ⬇️  Down arrow pressed")

def press_ctrl_home():
    print("      ⬆️  Moving to top of page (Ctrl + Home)")
    press_key_combination(Key.ctrl, Key.home)

def switch_to_next_tab():
    print("      🔄 Switching to next Chrome tab (Ctrl + Tab)")
    press_key_combination(Key.ctrl, Key.tab)

def alt_tab():
    print("      🔁 Toggling between windows (Alt + Tab)")
    press_key_combination(Key.alt, Key.tab)

def wait_with_countdown(seconds, message="⏱️ Waiting"):
    for remaining in range(seconds, -1, -1):  # go down to 0
        sys.stdout.write(f"\r{message}....[{remaining}/{seconds}] ")
        sys.stdout.flush()
        time.sleep(1)
    print()  # move to new line after countdown
