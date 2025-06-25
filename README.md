# 🚀 WorkActivity Automator

> **The Ultimate Human-like Activity Simulator for Productivity & Compliance**

---

Welcome to **WorkActivity Automator** — the professional-grade solution for simulating authentic user activity in Visual Studio Code and Google Chrome. Designed for organizations, teams, and individuals who need to keep sessions active, prevent idle timeouts, or demonstrate compliance with activity requirements.

---

## ✨ Key Features

- ⚙️ **Enterprise-Ready Automation**: Seamlessly simulate activity in VS Code and Chrome, with robust toggles for each environment.
- 🤖 **Human-like Randomization**: Advanced randomization of wait times and key presses to ensure natural, undetectable behavior.
- 🗂️ **Multi-Tab Chrome Workflow**: Effortlessly mimic real browsing by scrolling and switching across multiple Chrome tabs.
- 🛠️ **Effortless Customization**: All parameters (delays, durations, press counts) are easily configurable for your workflow.
- 🛑 **Safe & Graceful Exit**: Instantly halt automation with `Ctrl+C` — no risk to your system or data.
- 🖥️ **Live Console Feedback**: Real-time, color-coded logs for transparency and monitoring.
- 🔁 **Continuous Session Loop**: Designed for long-running, unattended operation in enterprise environments.
- 🏢 **Production-Grade Reliability**: Built for stability, clarity, and ease of integration into company workflows.

---

## 🧰 Requirements

- 🐍 Python 3.7+
- [pynput](https://pypi.org/project/pynput/) library

### 📦 Quick Install

```sh
pip install pynput
```

---

## 🚦 Quick Start

1. 🖥️ **Prepare Your Workspace**: Open Visual Studio Code and Google Chrome. Ensure `Alt+Tab` cycles only between these apps for best results.
2. ⚙️ **Configure Settings**: Adjust the variables at the top of WorkActivity_Automator.py to match your organization's needs (timings, session durations, automation toggles, etc.).
3. ▶️ **Run the Script**:
   ```sh
   python WorkActivity_Automator.py
   ```
4. 👀 **Monitor Activity**: Watch as the script simulates scrolling, tab switching, and window focus changes — all with human-like timing.
5. ✋ **Stop Anytime**: Press `Ctrl+C` in the terminal for an immediate, safe exit.

---

## 🛠️ Configuration Reference

| Setting                   | Description                                              |
|---------------------------|----------------------------------------------------------|
| `enable_vscode`           | Enable/disable VS Code automation                        |
| `enable_chrome`           | Enable/disable Chrome automation                         |
| `initial_delay`           | Wait time before automation starts (seconds)             |
| `vscode_session_duration` | Time spent in VS Code per round (seconds)                |
| `chrome_tab_time_total`   | Time per Chrome tab (seconds)                            |
| `chrome_tab_min/max`      | Number of Chrome tabs per round                          |
| `*_press_min/max`         | Down arrow presses per scroll event                      |
| `*_wait_min/max`          | Wait time between scroll events (seconds)                |
| `key_press_interval`      | Interval between individual key presses (seconds)        |

---

## 🧑‍💻 How It Works

- 📝 **VS Code**: Simulates scrolling by pressing the down arrow at random intervals.
- 🌐 **Chrome**: Scrolls and switches tabs, mimicking real browsing sessions.
- 🔄 **Window Switching**: Uses `Alt+Tab` to alternate between VS Code and Chrome.
- 🔁 **Session Loop**: Repeats the process for continuous, unattended operation.

---

## 💡 Best Practices & Tips

- 🪟 **Dedicated Workspace**: For maximum reliability, ensure only Chrome and VS Code are in the Alt+Tab cycle.
- 🧩 **Custom Actions**: Extend the script to support additional applications or more complex workflows.
- ⏱️ **Test First**: Start with short durations and intervals to validate your configuration.
- 🏢 **Compliance**: Use in accordance with your organization's IT and security policies.

---

## ⚠️ Legal & Compliance Notice

This software is provided for productivity, demonstration, and compliance purposes. Use only with proper authorization and in accordance with your organization's policies. The author assumes no liability for misuse or policy violations.

---

**👤 Author:** Soumya Ranjan Sahoo  
**🌐 License:** MIT  


