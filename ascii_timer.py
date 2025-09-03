import sys

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
