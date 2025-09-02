import time
import random
import sys
from pynput.keyboard import Key, Controller

keyboard = Controller()

# === CONFIGURABLE SETTINGS ===
# enable_vscode = False
# enable_chrome = True

initial_delay = 5  # Delay before the automation starts (in seconds)
vscode_session_duration = 600
chrome_tab_time_total = 60
chrome_tab_switch_reserved = 4
chrome_tab_session_duration = chrome_tab_time_total - chrome_tab_switch_reserved
chrome_tab_min = 1
chrome_tab_max = 3

vscode_press_min = 2
vscode_press_max = 8
vscode_wait_min = 8
vscode_wait_max = 13

chrome_press_min = 2
chrome_press_max = 5
chrome_wait_min = 8
chrome_wait_max = 10

key_press_interval = 0.3  # Applied globally

# === LOW-LEVEL KEY UTILITIES ===
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
        sys.stdout.write(f"\r{message}....{remaining} ")
        sys.stdout.flush()
        time.sleep(1)
    print()  # move to new line after countdown



# === LEVEL 2: VS CODE CONTROL ===
def control_vscode():
    print("\n🧠 Starting session in VS Code...")
    start_time = time.time()

    while time.time() - start_time < vscode_session_duration:
        press_count = random.randint(vscode_press_min, vscode_press_max)
        wait_time = random.randint(vscode_wait_min, vscode_wait_max)
        wait_with_countdown(wait_time, "   ⏱️ Waiting before scroll set")

        for _ in range(press_count):
            press_down_arrow()
            time.sleep(key_press_interval)

    print("✅ Completed activity in VS Code.\n")


# === LEVEL 3: CHROME TAB ACTIVITY ===
def chrome_tab_session():
    print("   📑 Simulating scroll activity in current Chrome tab...")
    tab_start = time.time()

    while time.time() - tab_start < chrome_tab_session_duration:
        press_count = random.randint(chrome_press_min, chrome_press_max)
        wait_time = random.randint(chrome_wait_min, chrome_wait_max)
        wait_with_countdown(wait_time, "   ⏱️ Waiting before scroll set")

        for _ in range(press_count):
            press_down_arrow()
            time.sleep(key_press_interval)

    press_ctrl_home()
    time.sleep(1)
    switch_to_next_tab()
    time.sleep(2)
    print("   ✅ Finished tab session.\n")

# === LEVEL 2: CHROME CONTROL ===
def control_chrome():
    print("\n🌐 Switching to Chrome and starting activity...")
    tab_count = random.randint(chrome_tab_min, chrome_tab_max)
    print(f"   🔁 Will simulate work on {tab_count} Chrome tab(s).\n")

    for tab_num in range(tab_count):
        print(f"   ▶️ Starting Chrome Tab #{tab_num + 1}")
        chrome_tab_session()

    print("✅ Completed activity in Chrome.\n")

# === BIG ASCII NUMBERS ===
BIG_NUMBERS = {
    '0': [" ██████ ",
          "██    ██",
          "██    ██",
          "██    ██",
          " ██████ "],
         
    '1': ["   ██   ",
          "  ███   ",
          "   ██   ",
          "   ██   ",
          " ██████ "],
         
    '2': ["███████ ",
          "     ██ ",
          "███████ ",
          "██      ",
          "███████ "],
         
    '3': [" ██████ ",
          "     ██ ",
          " ██████ ",
          "     ██ ",
          " ██████ "],
         
    '4': ["██   ██ ",
          "██   ██ ",
          "███████ ",
          "     ██ ",
          "     ██ "],
         
    '5': ["███████ ",
          "██      ",
          "███████ ",
          "     ██ ",
          "███████ "],
         
    '6': ["███████ ",
          "██      ",
          "███████ ",
          "██   ██ ",
          "███████ "],
         
    '7': ["███████ ",
          "     ██ ",
          "    ██  ",
          "   ██   ",
          "  ██    "],
         
    '8': [" █████  ",
          "██   ██ ",
          " █████  ",
          "██   ██ ",
          " █████  "],
         
    '9': ["███████ ",
          "██   ██ ",
          "███████ ",
          "     ██ ",
          "███████ "],
         
}

def print_big_timer(i, clear_lines=5):
    """Print big ASCII countdown timer with clean refresh"""
    num_str = str(i)
    lines = [""] * 5
    for digit in num_str:
        digit_art = BIG_NUMBERS.get(digit, ["      "] * 5)
        for idx in range(5):
            lines[idx] += digit_art[idx] + "  "
    timer_art = "\n".join(lines)

    # Move cursor up & clear old output
    sys.stdout.write("\033[F" * clear_lines)
    sys.stdout.write("\033[J")

    sys.stdout.write(f"{timer_art}\n")
    sys.stdout.flush()

# === MAIN SIMULATOR LOOP ===
def main_simulator():
    print("🚀 Welcome to the Automated Work Activity Simulator!")
    print("💡 Keep your workspace ready (Chrome + VS Code) before starting.")
    print("The 1st window should be VS Code, 2nd should be Chrome.")

    def ask_yes_no(prompt, default="y"):
        """Ask user yes/no and return True/False"""
        choice = input(f"{prompt} (y/n) [default: {default}]: ").strip().lower()
        if choice == "":
            choice = default
        return choice.startswith("y")

    enable_vscode = ask_yes_no("👉 Do you want to enable VS Code automation?")
    enable_chrome = ask_yes_no("👉 Do you want to enable Chrome automation?")

    print(f"Enable VS Code: {enable_vscode}\nEnable Chrome: {enable_chrome}")
    print(f"⏳ Initialization delay: {initial_delay} seconds...\n")

    # Reserve space for timer output
    print("\n" * 6, end="")

    # Countdown
    for i in range(initial_delay, 0, -1):
        print_big_timer(i)
        time.sleep(1)

    # Final clear
    sys.stdout.write("\033[F" * 6)
    sys.stdout.write("\033[J")
    sys.stdout.flush()
    print("✅ Countdown finished!\n")

    round_count = 1
    try:
        while True:
            print(f"\n======================")
            print(f"🎬 ROUND #{round_count} START")
            print(f"======================")

            if enable_vscode:
                control_vscode()

            if enable_chrome:
                print("   🔄 Switching to Chrome...")
                alt_tab()
                control_chrome()
                print("   🔄 Switching to VS Code...")
                alt_tab()

            print(f"🌀 ROUND #{round_count} COMPLETED")
            print("========================\n")
            round_count += 1

    except KeyboardInterrupt:
        print("\n🛑 Simulation interrupted. Exiting gracefully...")

# === RUN SCRIPT ===
main_simulator()
