import colorama
import random
import msvcrt

colorama.init()
colors = list(vars(colorama.Fore).values())

while True:
    char = msvcrt.getch().decode('utf-8', errors='ignore')

    if char == '\r':
        print()
        continue
    
    colored_char = random.choice(colors) + char + colorama.Fore.RESET
    print(colored_char, end='', flush=True)
    
colorama.deinit()