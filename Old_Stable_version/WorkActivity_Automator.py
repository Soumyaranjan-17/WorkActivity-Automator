import time
import random
from pynput.keyboard import Key, Controller

keyboard = Controller()

# === CONFIGURABLE SETTINGS ===
# --- Enable/Disable Sections ---
enable_vscode = True
enable_chrome = False

# --- General ---
initial_delay = 10  # Delay before the automation starts (in seconds)
vscode_session_duration =  600 # Total time spent in VS Code (in seconds)
chrome_tab_time_total = 15  # Total time spent per Chrome tab (in seconds)
chrome_tab_switch_reserved = 4  # Reserved seconds for Ctrl+Home and Ctrl+Tab
chrome_tab_session_duration = chrome_tab_time_total - chrome_tab_switch_reserved
chrome_tab_min = 1  # Minimum number of Chrome tabs per round
chrome_tab_max = 3  # Maximum number of Chrome tabs per round

# --- VS Code Settings ---
vscode_press_min = 2
vscode_press_max = 5
vscode_wait_min = 10
vscode_wait_max = 15

# --- Chrome Settings ---
chrome_press_min = 2
chrome_press_max = 5
chrome_wait_min = 10
chrome_wait_max = 15 #should be less than chrome_tab_time_total

# --- Unified Key Press Interval ---
key_press_interval = 0.1  # Applied globally

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

# === LEVEL 2: VS CODE CONTROL ===
def control_vscode():
    print("\n🧠 Starting session in VS Code...")
    start_time = time.time()

    while time.time() - start_time < vscode_session_duration:
        press_count = random.randint(vscode_press_min, vscode_press_max)
        print(f"   ⏱️ Waiting {random.randint(vscode_wait_min, vscode_wait_max)} seconds before scroll set...")
        time.sleep(random.randint(vscode_wait_min, vscode_wait_max))

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
        print(f"      ⏱️ Waiting {wait_time} seconds before scroll set...")
        time.sleep(wait_time)

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
    

# === MAIN SIMULATOR LOOP ===
def main_simulator():
    print("🚀 Welcome to the Automated Work Activity Simulator!")
    print("💡 Keep your workspace ready (Chrome + VS Code) before starting.")
    print(f"⏳ Initialization delay: {initial_delay} seconds...\n")
    for i in range(initial_delay, 0, -1):
        print(f"   ⏱️ {i}...")
        time.sleep(1)

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
