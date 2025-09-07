import time
import random
import sys
from ascii_timer import print_big_timer
from utility import *
from configuration import *

speedometer = {
    "vscode": (vscode_press_min + vscode_press_max) / 2 / ((vscode_wait_min + vscode_wait_max) / 2 + key_press_interval * ((vscode_press_min + vscode_press_max) / 2)),
    "chrome": (chrome_press_min + chrome_press_max) / 2 / ((chrome_wait_min + chrome_wait_max) / 2 + key_press_interval * ((chrome_press_min + chrome_press_max) / 2))
}

print(f"⚙️  Speedometer Settings:")
print(f"   - VS Code: ~{speedometer['vscode']:.2f} key presses/sec")
print(f"   - Chrome: ~{speedometer['chrome']:.2f} key presses/sec\n")

def chrome_tab_session():
    print("   📑 Simulating scroll activity in current Chrome tab...")
    tab_start = time.time()

    while time.time() - tab_start < chrome_tab_session_duration:
        press_count = random.randint(chrome_press_min, chrome_press_max)
        wait_time = random.randint(chrome_wait_min, chrome_wait_max)
        wait_with_countdown(wait_time, "   🟠 Waiting in Chrome")

        for _ in range(press_count):
            press_down_arrow()
            time.sleep(key_press_interval)

    press_ctrl_home()
    time.sleep(1)
    switch_to_next_tab()
    time.sleep(2)
    print("   ✅ Finished tab session.\n")

def vscode_tab_session():
    print("   💻 Simulating scroll activity in current VS Code tab...")
    tab_start = time.time()

    while time.time() - tab_start < vscode_tab_session_duration:
        press_count = random.randint(vscode_press_min, vscode_press_max)
        wait_time = random.randint(vscode_wait_min, vscode_wait_max)
        wait_with_countdown(wait_time, "   🟢 Waiting in VS Code")

        for _ in range(press_count):
            press_down_arrow()
            time.sleep(key_press_interval)

    press_ctrl_home()
    time.sleep(1)
    switch_to_next_tab()
    time.sleep(2)


# === LEVEL 2: CHROME CONTROL ===
def control_chrome():
    print("\n🌐 Switching to Chrome and starting activity...")
    tab_count = random.randint(chrome_tab_min, chrome_tab_max)
    print(f"   🔁 Will simulate work on {tab_count} Chrome tab(s).\n")

    for tab_num in range(tab_count):
        print(f"   ▶️ Starting Chrome Tab #{tab_num + 1}")
        chrome_tab_session()

    print("✅ Completed activity in Chrome.\n")

def control_vscode():
    print("\n💻 Switching to VS Code and starting activity...")
    tab_count = random.randint(vscode_tab_min, vscode_tab_max)
    print(f"   🔁 Will simulate work on {tab_count} VS Code tab(s).\n")

    for tab_num in range(tab_count):
        print(f"   ▶️ Starting VS Code Tab #{tab_num + 1}")
        vscode_tab_session()

    print("✅ Completed activity in VS Code.\n")


# === MAIN SIMULATOR LOOP ===
def main_simulator():
    print("🚀 Welcome to the Automated Work Activity Simulator!")
    print("💡 Keep your workspace ready (Chrome + VS Code) before starting.")
    print("The 1st window should be VS Code, 2nd should be Chrome.")

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
