initial_delay = 5  # Delay before the automation starts (in seconds)

vscode_session_duration = 600
chrome_tab_time_total = 60

chrome_tab_switch_reserved = 4
chrome_tab_session_duration = chrome_tab_time_total - chrome_tab_switch_reserved
chrome_tab_min = 1
chrome_tab_max = 3

vscode_tab_switch_reserved = 4
vscode_tab_session_duration = vscode_session_duration - vscode_tab_switch_reserved
vscode_tab_min = 1
vscode_tab_max = 3

vscode_press_min = 2
vscode_press_max = 8
vscode_wait_min = 5
vscode_wait_max = 10

chrome_press_min = 2
chrome_press_max = 5
chrome_wait_min = 5
chrome_wait_max = 10

key_press_interval = 0.3  # Applied globally