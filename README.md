

# 🚀 WorkActivity-Automator

Automate and simulate work activity in VS Code and Chrome using keyboard and mouse events. Useful for keeping sessions active, testing automation, or simulating user activity.

---

## 📚 Table of Contents

- [📖 Description](#description)
- [✨ Features](#features)
- [🛠️ Installation](#installation)
- [🎮 Usage](#usage)
- [⚙️ Configuration](#configuration)
- [📂 File Overview](#file-overview)
- [💡 Example Use Cases](#example-use-cases)
- [👍 Pros & 👎 Cons](#pros--cons)
- [🤝 Contributing](#contributing)
- [📝 License](#license)
- [📬 Contact](#contact)

---

## 📖 Description

WorkActivity-Automator is a Python tool that simulates user activity in VS Code and Chrome by automating keyboard and mouse events. It is designed to keep your sessions alive, test automation scripts, or simply have fun with workspace automation. 😄

---

## ✨ Features

- 🤖 Simulates scrolling and tab switching in VS Code and Chrome
- ⏱️ ASCII countdown timer before starting
- 🛠️ Configurable session durations, tab counts, and key press intervals
- 🧩 Interactive prompts to enable/disable automation for VS Code and Chrome
- 🏎️ Speedometer for key presses per second
- 🖱️ Mouse scroll automation example
- 📦 Includes previous stable versions for reference

---

## 🛠️ Installation

### Requirements

- 🐍 Python 3.7+
- 📦 `pynput` library

Install dependencies:
```bash
pip install pynput
```

---

## 🎮 Usage

1. 🖥️ Ensure Chrome and VS Code are open (VS Code as the first window, Chrome as the second).
2. ▶️ Run the main script:
	```bash
	python main.py
	```
3. 🤓 Follow the interactive prompts to enable/disable automation for VS Code and Chrome.
4. 🔄 The script will simulate activity in the selected applications, switching tabs and scrolling as configured.

---

## ⚙️ Configuration

Edit `configuration.py` to adjust:

- ⏳ Initial delay before starting
- 🕒 Session durations
- 🗂️ Tab counts
- ⌨️ Key press intervals
- ⏱️ Wait times

---

## 📂 File Overview

- `main.py`: 🚦 Main automation script. Handles user prompts, session logic, and orchestrates activity simulation.
- `configuration.py`: ⚙️ Stores all configurable parameters (delays, durations, tab counts, intervals).
- `utility.py`: 🧰 Provides keyboard utility functions (key combinations, tab switching, countdowns, etc.).
- `ascii_timer.py`: ⏲️ Prints large ASCII countdown timers for visual feedback.
- `mouse_controller.py`: 🖱️ Example script for mouse scroll automation.
- `Old_Stable_version/`: 📦 Contains previous stable versions of the automator for reference.

---

## 💡 Example Use Cases

- 🛡️ Keep your remote session alive (no more auto-logout!)
- 🤪 Prank your friends by making their VS Code and Chrome go wild
- 🧪 Test automation scripts for keyboard/mouse events
- 🎬 Simulate user activity for demos or presentations
- 🕵️‍♂️ Make your workspace look busy (we won't tell your boss 😉)

---

## 👍 Pros & 👎 Cons

### 👍 Pros
- 🚀 Easy to use
- 🛠️ Highly configurable
- 😃 Fun and interactive
- 🌍 Open source — contributions welcome!

### 👎 Cons
- ⚠️ May interfere with your actual work if left running
- 🐍 Requires Python and `pynput` installed
- 💤 Not a replacement for real productivity

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request. For major changes, please open a discussion first. Let's automate together! 🚀

---

## 📝 License

This project is licensed under the MIT License.

---

## 📬 Contact

Created by [Soumyaranjan-17](https://github.com/Soumyaranjan-17). For questions or collaboration, feel free to reach out via GitHub.

---

Happy automating! If you enjoyed this project, give it a ⭐ on GitHub and share with your friends! 😃
