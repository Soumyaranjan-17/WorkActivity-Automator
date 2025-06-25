# WorkActivity Automator

A Python tool to simulate human-like activity in Visual Studio Code and Google Chrome by automating keyboard actions. This utility is ideal for keeping sessions active, preventing idle timeouts, or for demonstration and testing purposes.

## Features
- **Configurable Automation**: Enable or disable activity simulation for VS Code and Chrome independently.
- **Human-like Randomization**: Wait times and key presses are randomized within user-defined ranges to mimic natural behavior.
- **Multi-Tab Chrome Support**: Simulates activity across multiple Chrome tabs, including scrolling and tab switching.
- **Easy Customization**: All key parameters (delays, durations, press counts) are set at the top of the script for quick adjustment.
- **Graceful Exit**: Press `Ctrl+C` in the terminal to stop the simulation at any time.
- **Clear Console Output**: Provides real-time feedback on actions being performed.
- **Session Loop**: Repeats the process in rounds until interrupted, for continuous simulation.

## Requirements
- Python 3.x
- [pynput](https://pypi.org/project/pynput/) library

### Install dependencies
```sh
pip install pynput
```

## Usage
1. **Prepare Your Workspace**: Open both Visual Studio Code and Google Chrome. Arrange them so that `Alt+Tab` switches between them easily.
2. **Configure Settings**: Edit the variables at the top of `WorkActivity_Automator.py` to suit your needs (e.g., enable/disable Chrome or VS Code automation, adjust timings, session durations, etc.).
3. **Run the Script**:
   ```sh
   python WorkActivity_Automator.py
   ```
4. **Observe Automation**: The script will begin after an initial delay, then alternate between VS Code and Chrome (if enabled), simulating scrolling and tab switching.
5. **Stop Anytime**: Press `Ctrl+C` in the terminal to exit.

## Key Settings
- `enable_vscode`, `enable_chrome`: Toggle automation for each app.
- `initial_delay`: Wait time before automation starts.
- `vscode_session_duration`: Total time spent in VS Code per round.
- `chrome_tab_time_total`: Time per Chrome tab.
- `chrome_tab_min`, `chrome_tab_max`: Number of Chrome tabs per round.
- `*_press_min`, `*_press_max`: Number of down arrow presses per scroll event.
- `*_wait_min`, `*_wait_max`: Wait time between scroll events.
- `key_press_interval`: Interval between individual key presses.

## How It Works
- **VS Code**: Simulates random down arrow key presses at intervals, mimicking scrolling through code.
- **Chrome**: For each tab, simulates scrolling, then switches to the next tab using `Ctrl+Tab`.
- **Window Switching**: Uses `Alt+Tab` to alternate between VS Code and Chrome.
- **Session Loop**: Repeats the process in rounds until interrupted.

## Tips
- For best results, ensure Chrome and VS Code are the only windows in the Alt+Tab cycle.
- You can further customize the script to add more actions or support other applications.
- Test with short durations and intervals before using longer sessions.
- Run the script in a dedicated workspace to avoid interfering with other applications.

## Disclaimer
This script is for educational, demonstration, or testing purposes only. Use responsibly and in accordance with your organization's policies.

---

**Author:** Soumya Ranjan Sahoo

